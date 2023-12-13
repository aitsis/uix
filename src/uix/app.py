
from .core.flask_server import FlaskServer
from .core.htmlgen import HTMLGen
from .core.session import Session
from uuid import uuid4
import os
class UIX:
    def __init__(self):
        FlaskServer.static_files_path = os.path.join(os.path.dirname(__file__), "static")
        self.ui = None
        self.server = None
        self.index_gen = HTMLGen()
        self.sessions = {}


    def index(self):
        session_id = str(uuid4())
        session = Session()
        self.sessions[session_id] = session
        html = self.index_gen.generate()
        cookie = {'session_id': session_id}
        return html, cookie
    
   

    def start(self, ui = None, port=5000, host="0.0.0.0", debug=False):
        self.ui = ui
        if self.server is None:
            self.server = FlaskServer(port, host, debug)
            self.server.set_index_handler(self.index)
            self.server.set_socket_handler("connect", self.socket_on_connect)
            self.server.start()

    
    def socket_on_connect(self):
        session_id = self.server.get_cookie("session_id")
        session = self.sessions[session_id]
        session.init(self.ui, session_id)
        