import threading

class Context(threading.local):
    def __init__(self, session, threadId, requestData):
        self.session = session
        self.threadId = threadId
        self.elements = session.elements
        self.data = {}
        self.data["cookies"] = requestData["cookies"]
