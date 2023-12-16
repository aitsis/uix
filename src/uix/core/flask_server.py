import os
import tempfile
from functools import wraps
from uuid import uuid4
from threading import Lock
from flask import Flask, request, send_from_directory, abort, jsonify, make_response
from flask_cors import CORS  # type: ignore
from flask_socketio import SocketIO  # type: ignore
import logging
from uix.core.web_server import Server


class FlaskServer(Server):
    static_files_path = None # set on UIX
    def __init__(self, port=5000, host = "0.0.0.0", debug=False):
        super().__init__(port, host,debug)
        if debug == False:
            log = logging.getLogger('werkzeug')
            log.disabled = True
        self.app = Flask(__name__)
        self.host = host
        self.socketio = SocketIO(self.app, cors_allowed_origins="*", transports=["websocket"],engineio_logger=True, logger=True)
        CORS(self.app)
        self.app.add_url_rule("/", "index", self._index)
        self.app.add_url_rule("/<path:path>", "static_files", FlaskServer.static_files)
        self.app.add_url_rule("/api/<path:path>", "api", self.api, methods=["POST"])
        self.index = None
        self.socketio.on_event("connect", self._socketio_on_connect)
        self.socketio.on_event("disconnect", self._socketio_on_disconnect)
        self.socketio.on_event("from_client", self._socketio_on_client)

    @staticmethod
    def static_files(path):
        response = send_from_directory(FlaskServer.static_files_path, path)
        return response

    def api(self, path):
        return "Hello World from API!"
    
    def _index(self):
        if self.index is None:
            return "Undefined index handler."
        else:
            return self.index()
            
        
    def start(self):
        self.app.run(port=self.port, host=self.host, threaded=True, debug=self.debug)

    def set_index_handler(self, handler):
        self.index = handler
    
    def stop(self):
        self.socketio.stop()
        self.app.stop()
    
    def emit(self, event, data, room=None):
        self.socketio.emit(event, data, room=room)
        
    def _socketio_on_connect(self):
        print("Client connected: ", request.args.get('session_id'))
        if self.socket_on_connect:
            sid = request.args.get('session_id')
            #clientPublicData = request.args.get('clientPublicData')
            #socket_on_connect(sid, clientPublicData)
            self.socket_on_connect(sid)
    
    def _socketio_on_disconnect(self):
        if self.socket_on_disconnect:
            sid = request.args.get('session_id')
            self.socket_on_disconnect(sid)

    def _socketio_on_client(self, data):
        print("Client sent: ", data)
        if self.socket_on_client:
            print("Client sent2: ", data)
            sid = request.args.get('session_id')
            self.socket_on_client(sid,data)

    def get_cookie(self, name):
        return request.cookies.get(name)