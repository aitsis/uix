from uuid import uuid4
import os
import logging
# FLASK SERVER -------------------------------------------------------------------------------------
from flask import Flask, request, send_from_directory, abort, jsonify, make_response
from flask_cors import CORS
from flask_socketio import SocketIO
# UIX CORE -----------------------------------------------------------------------------------------
from .core.htmlgen import HTMLGen
from .core.session import Session

# GLOBALS ------------------------------------------------------------------------------------------
static_files_path = os.path.join(os.path.dirname(__file__), "static")
ui_root = None
ui_parent = None
sessions = {}
html = HTMLGen()
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
    if sid in sessions:
        sessions[sid].clientHandler(data)
    
         


# START --------------------------------------------------------------------------------------------
def start(ui = None, port=5000, host="0.0.0.0", debug=False, threaded=True):
    global ui_root
    ui_root = ui
    flask.run(port=port, host=host, threaded=threaded, debug=debug)
