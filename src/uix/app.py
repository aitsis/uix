from typing import List
from uuid import uuid4
import os
import logging
# FLASK SERVER -------------------------------------------------------------------------------------
from flask import Flask, request, send_from_directory, abort, jsonify, Response
from flask_cors import CORS
from flask_socketio import SocketIO
# UIX CORE -----------------------------------------------------------------------------------------
from .core.htmlgen import HTMLGen
from .core.session import Session
from ._config import config
from .core.pipe import Pipe
# GLOBALS ------------------------------------------------------------------------------------------
static_files_path = os.path.join(os.path.dirname(__file__), "static")
log_handler = None
error_handler = None
ui_root = None
ui_parent = None
sessions = {}
html = HTMLGen()
_pipes: List[Pipe] = []


# SERVER -------------------------------------------------------------------------------------------
flask = Flask(__name__)
socketio = SocketIO(flask, cors_allowed_origins="*", transports=["websocket"])
CORS(flask)

# ROUTES -------------------------------------------------------------------------------------------
# INDEX
@flask.route("/")
def index():
    return html.generate()

# STATIC FILES
@flask.route("/<path:path>")
def static_files(path):
        return send_from_directory(static_files_path, path)

def add_static_route(logical_path, local_directory):
    flask.add_url_rule(f"/{logical_path}/<path:path>", local_directory, lambda path : send_from_directory(local_directory, path))

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
    print("download:",path)
    if path in files:
        print("download:",path,"found")
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
    sessions[sid] = Session(sid)

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