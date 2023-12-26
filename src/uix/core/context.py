import threading

class Context(threading.local):
    def __init__(self, session, threadId):
        self.session = session
        self.threadId = threadId
        self.elements = session.elements
        self.data = {}
