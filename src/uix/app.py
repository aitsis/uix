from uuid import uuid4
from .core.flask_server import FlaskServer
from .core.htmlgen import HTMLGen
from .core.session import Session
import os

class UIX:
    def __init__(self):
        FlaskServer.static_files_path = os.path.join(os.path.dirname(__file__), "static")
        self.ui_root = None
        self.server = None
        self.sessions = {}

    def index(self):
        # if(self.ui_root is None):
        #     return "UIX Not Initialized"
        sid = str(uuid4())
        session = Session(sid, self.ui_root,self)
        self.sessions[sid] = session
        html = session.index.generate(sid)
        return html
    
    def start(self, ui = None, port=5000, host="0.0.0.0", debug=False):
        self.ui_root = ui
        if self.server is None:
            self.server = FlaskServer(port, host, debug)
            self.server.set_index_handler(self.index)
            self.server.socket_on_connect = self.socket_on_connect
            self.server.socket_on_disconnect = self.socket_on_disconnect
            self.server.socket_on_client = self.socket_on_client
            self.server.start()


    def socket_on_connect(self, sid):
        if sid in self.sessions:
            session = self.sessions[sid]
            

    def socket_on_disconnect(self, sid):
        if sid in self.sessions:
            session = self.sessions[sid]
            session.close()
            del self.sessions[sid]

    def socket_on_client(self, sid, data):
        if sid in self.sessions:
            print(data,sid)
            session = self.sessions[sid]
            session.clientHandler(data)

uix_app = UIX()