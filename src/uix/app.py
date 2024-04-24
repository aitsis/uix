from typing import List
from uuid import uuid4
import os
import json
import logging
# FLASK SERVER -------------------------------------------------------------------------------------
from flask import Flask, request, send_from_directory, abort, jsonify, Response, make_response, redirect, send_file
from flask_cors import CORS
from flask_socketio import SocketIO
# UIX CORE -----------------------------------------------------------------------------------------
from .core.htmlgen import HTMLGen
from .core.session import Session
from ._config import config
from .core.pipe import Pipe
from .core.cookie import build_cookieJar_from_dict, extract_cookie_settings_from_request_args
# GLOBALS ------------------------------------------------------------------------------------------
static_files_path = os.path.join(os.path.dirname(__file__), "static")
log_handler = None
error_handler = None
ui_root = None
sessions = {}
api_handlers = {}
html = HTMLGen()
_pipes: List[Pipe] = []
on_session_init = None

# SERVER -------------------------------------------------------------------------------------------
flask = Flask(__name__)
socketio = SocketIO(flask, cors_allowed_origins="*", transports=["pooling","websocket"])
CORS(flask)

# ROUTES -------------------------------------------------------------------------------------------
# INDEX
@flask.route("/")
def index():
     return html.generate()

# INDEX_PATH
@flask.route("/<path:path>")
def index_with_path(path):
    return html.generate()

@flask.route('/logout', methods=['GET'])
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('__u_at', '', expires=0, path='/', samesite='Strict')
    response.set_cookie('__u_ref', '', expires=0, path='/', samesite='Strict')
    return response

# SET COOKIE FROM QUERY STRING
@flask.route('/set-cookie', methods=['GET'])
def set_cookie():
    """
    Handles setting a cookie based on provided query parameters.
    Returns a 204 No Content response on success.
    *DO NOT USE FOR SENSITIVE COOKIES*

    Examples URLs:
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&max_age=3600
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&path=/
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&domain=127.0.0.1
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&expires=1711877452
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&expires=1711877452&secure=true&httponly=true&samesite=strict
    """
    try:
        cookie_settings = extract_cookie_settings_from_request_args(request.args)

        if not cookie_settings['key'] or not cookie_settings['value']:
            return jsonify({'error': 'Both key and value are required'}), 400

        response = make_response()
        response.set_cookie(**cookie_settings)
        response.status_code = 204
        return response

    except Exception as e:
        logging.error(f"Error setting cookie: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# SET COOKIE FROM REQUEST BODY
@flask.route('/set-cookieS', methods=['POST'])
def set_cookie_secure():
    """
    Handles setting a cookie.
    Returns a 204 No Content response on success.

    Example Request Data (JSON):
    ```json
    {
        "route": "/set-cookieS",
        "method": "POST",
        "cookie_settings": {
            "key": "cookie_name",
            "value": "value",
            "expires": 1713278615,
            "httponly": true
        }
    }
    ```
    """
    try:
        cookie_settings = json.loads(request.data)['cookie_settings']

        if not cookie_settings['key'] or not cookie_settings['value']:
            return jsonify({'error': 'Both key and value are required'}), 400
        
        response = make_response()
        response.set_cookie(**cookie_settings)
        response.status_code = 204
        return response

    except Exception as e:
        logging.error(e)
        return jsonify({'error': 'Internal server error'}), 500

# API ENDPOINT
def register_api_handler(name, handler):
    api_handlers[name] = handler
@flask.route("/manual_api/<path:path>")
def api_func(path):
    paths = path.split("/")
    if paths[0] in api_handlers:
        response = make_response(api_handlers[paths[0]](paths, request.args))
        response.headers['Cache-Control'] = 'max-age=31536000'
        return response
    else:
        return abort(404)
# STATIC FILES
@flask.route("/static/<path:path>")
def static_files(path):
    response = make_response(send_from_directory(static_files_path, path))
    response.headers['Cache-Control'] = 'max-age=31536000'
    return response

def _send_from_directory(directory, path):
    response = make_response(send_from_directory(directory, path))
    response.headers['Cache-Control'] = 'max-age=31536000'
    return response


def add_static_route(logical_path, local_directory):
    flask.add_url_rule(f"/{logical_path}/<path:path>", local_directory, lambda path : _send_from_directory(local_directory, path))

# UPLOAD ENDPOINT
files = {}
@flask.route("/upload/<path:path>", methods=["POST"])
def upload(path):
    if(request.data):
        files[path] = {"data": request.data, "type": request.mimetype}
        return jsonify({"success": path})
    else:
        return abort(400)

# DOWNLOAD ENDPOINT
@flask.route("/download/<path:path>", methods=["GET"])
def download(path):
    #print("download:",path)
    if path in files:
        #print("download:",path,"found")
        datadict = files[path]
        return Response(datadict["data"], mimetype=datadict["type"])
    else:
        print("download:",path,"not found")
        return abort(404)

# SOCKETIO -----------------------------------------------------------------------------------------
@socketio.on("connect")
def socket_on_connect():
    print("Client Connected")
    sid = request.sid
    cookieJar = build_cookieJar_from_dict(request.cookies)
    requestData = {
      "cookies" : cookieJar,
      "headers" : request.headers
    }
    sessions[sid] = Session(sid, requestData=requestData)

@socketio.on("disconnect")
def socket_on_disconnect():
    sid = request.sid
    if sid in sessions:
        del sessions[sid]

@socketio.on("from_client")
def socket_on_client(data):
    sid = request.sid
    for pipe in _pipes:
        data = pipe.run(sid, data)
    if sid in sessions:
        sessions[sid].clientHandler(data)

def log(*args):
    if log_handler is not None:
        log_handler(*args)
    else:
        if config["debug"]:
            print(*args)

def error(*args):
    if error_handler is not None:
        error_handler(*args)
    else:
        print(*args)

def init_app(uix_config):
    global config
    # DEFAULT CONFIG --------------------------------------------------------------------------------
    config["host"] = "0.0.0.0"
    config["port"] = 5000
    config["threaded"] = True
    config["debug"] = False
    config["pipes"] = []
    config["locales_path"] = None
    # CONFIG ----------------------------------------------------------------------------------------
    if uix_config is not None:
        for key in uix_config:
            print(key)
            config[key] = uix_config[key]
    # INIT PIPES -----------------------------------------------------------------------------------
    for pipe in config["pipes"]:
        _pipes.append(pipe)
    
    
def get_start_example():
    from .example import start_example
    return start_example

def flask_run():
    flask.run(port=     config["port"],
              host=     config["host"],
              threaded= config["threaded"],
              debug =   config["debug"])
# START --------------------------------------------------------------------------------------------
def start(ui = None, config = None):
    global ui_root
    ui_root = ui if ui is not None else get_start_example() 
    init_app(config)
    flask_run()