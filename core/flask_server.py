import os
import tempfile
from functools import wraps
from uuid import uuid4
from threading import Lock
from flask import Flask, request, send_from_directory, abort, jsonify, make_response
from flask_cors import CORS  # type: ignore
from flask_socketio import SocketIO  # type: ignore

# DISABLE LOGGING
import logging
from uix.core.web_server import Server

# Add the missing import for the Server class
logging.getLogger('werkzeug').disabled = True


class FlaskServer(Server):
    def __init__(self, port=5000, host = "0.0.0.0", debug=False):
        super().__init__(port, host,debug)
        self.app = Flask(__name__)
        #self.socketio = SocketIO(self.app, cors_allowed_origins="*", transports=["websocket"])
        CORS(self.app)
        #self.socketio.on("connect", self.on_socket_connect)
        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/<path:path>", "static_files", FlaskServer.static_files)
        self.app.add_url_rule("/api/<path:path>", "api", self.api, methods=["POST"])

    @staticmethod
    def static_files(path):
        response = send_from_directory("static", path)
        response.headers['Cache-Control'] = 'max-age=31536000'
        return response

    def api(self, path):
        return "Hello World from API!"
    
    def index(self):
        return "Hello World!"
    
    def start(self):
        self.app.run(port=self.port, host=self.host, threaded=True, debug=self.debug)
