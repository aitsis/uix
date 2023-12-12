
from .core.flask_server import FlaskServer

server = None

def start(port=5000, host="0.0.0.0",debug=False):
    global server
    server = FlaskServer(port, host,debug)
    server.start()

if __name__ == '__main__':
    start()


    
