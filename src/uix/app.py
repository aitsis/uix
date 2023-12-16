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
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", transports=["websocket"],engineio_logger=True, logger=True)
CORS(app)

# ROUTES -------------------------------------------------------------------------------------------
# INDEX
@app.route("/")
def index():
    sid = str(uuid4())
    session = Session(sid, ui_root,app)
    sessions[sid] = session
    html = session.index.generate(sid)
    return html

# STATIC FILES
@app.route("/<path:path>")
def static_files(path):
        return send_from_directory(static_files_path, path)

# SOCKETIO -----------------------------------------------------------------------------------------
@socketio.on("connect")
def socket_on_connect():
    print("Client connected: ", request.args.get('session_id'))
    sid = request.args.get('session_id')
    if sid in sessions:
        session = sessions[sid]

@socketio.on("disconnect")
def socket_on_disconnect():
    sid = request.args.get('session_id')
    if sid in sessions:
        session = sessions[sid]
        session.close()
        del sessions[sid]

@socketio.on("from_client")
def socket_on_client(data):
    sid = request.args.get('session_id')
    if sid in sessions:
        print(data,sid)
        session = sessions[sid]
        session.clientHandler(data)

# START --------------------------------------------------------------------------------------------
def start(ui = None, port=5000, host="0.0.0.0", debug=False, threaded=True):
    global ui_root
    ui_root = ui
    app.run(port=port, host=host, threaded=threaded, debug=debug)
