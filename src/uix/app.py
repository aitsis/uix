
from .core.flask_server import FlaskServer
from .core.htmlgen import HTMLGen
import os
class UIX:
    def __init__(self):
        FlaskServer.static_files_path = os.path.join(os.path.dirname(__file__), "static")
        self.server = None
        self.index_gen = HTMLGen()


    def index(self):
        return self.index_gen.generate()

    def start(self, ui = None, port=5000, host="0.0.0.0", debug=False):
        if self.server is None:
            self.server = FlaskServer(port, host, debug)
            self.server.set_index_handler(self.index)
            self.server.start()

    
