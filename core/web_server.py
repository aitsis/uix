#web_server.py
# for isolating the server code

class Server:
    def __init__(self, port = 5000, host = "0.0.0.0",debug=False):
        self.port = port
        self.host = host
        self.debug = debug

    def start(self):
        pass

    def stop(self):
        pass
