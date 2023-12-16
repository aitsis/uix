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
sessions = {}

# SERVER -------------------------------------------------------------------------------------------
flask = Flask(__name__)
socketio = SocketIO(flask, cors_allowed_origins="*", transports=["websocket"],engineio_logger=True, logger=True)
CORS(flask)

# ROUTES -------------------------------------------------------------------------------------------
# INDEX
@flask.route("/")
def index():
    session_id = str(uuid4())
    session = Session(session_id, ui_root)
    sessions[session_id] = session
    html = session.index.generate(session_id)
    return html

# STATIC FILES
@flask.route("/<path:path>")
def static_files(path):
        return send_from_directory(static_files_path, path)

# SOCKETIO -----------------------------------------------------------------------------------------
@socketio.on("connect")
def socket_on_connect():
    print("Client connected: ", request.args.get('session_id'))
    session_id = request.args.get('session_id')
    if session_id in sessions:
        session = sessions[session_id]
        session.sid = request.sid


@socketio.on("disconnect")
def socket_on_disconnect():
    session_id = request.args.get('session_id')
    if session_id in sessions:
        session = sessions[session_id]
        session.close()
        del sessions[session_id]

@socketio.on("from_client")
def socket_on_client(data):
    session_id = request.args.get('session_id')
    if session_id in sessions:
        print(data,session_id)
        session = sessions[session_id]
        session.clientHandler(data)

# START --------------------------------------------------------------------------------------------
def start(ui = None, port=5000, host="0.0.0.0", debug=False, threaded=True):
    global ui_root
    ui_root = ui
    flask.run(port=port, host=host, threaded=threaded, debug=debug)
