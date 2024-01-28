
import threading
import uix
from copy import deepcopy
from .context import Context
context = threading.local()

class Session:
    def __init__(self,sid):
        self.sid = sid
        self.locale = None
        self.ui_root = None
        self._next_id = 0
        self.elements = {}
        self.message_queue = []
        self.context = Context(self, None)

    def InitializeClient(self):
        uix.log("Client Initialized")
        if( uix.app.ui_root is not None):
            self.ui_root = deepcopy(uix.app.ui_root)
            self.ui_root.bind(self)
            html = self.ui_root.render()
            self.send("ait-uix", html, "init-content")
            self.ui_root._init()
            self.flush_message_queue()
        else:
            uix.error("No UI Root")

    def eventHandler(self, data):
        id = data["id"]
        if id in self.elements:
            elm = self.elements[id]
            if elm is not None:
                event_name = data["event_name"]
                if event_name in elm.events:
                    self.context.element = elm
                    if "value" in data:
                        elm.events[event_name](self.context, id, data["value"])
                    else:
                        #uix.error("No value in event. name :", event_name, "id:", id, "data:", data)
                        elm.events[event_name](self.context, id, None)

    def clientHandler(self, data):
        if data["id"] == "ait-uix" and data["value"] == "init":
            self.InitializeClient()
            context.session = self
            if uix.app.on_session_init is not None:
                uix.app.on_session_init(context)
        else:    
            self.eventHandler(data)
    
    def push_parent(self, parent):
        self.parent_stack.append(parent)

    def pop_parent(self):
        return self.parent_stack.pop()

    def current_parent(self):
        return self.parent_stack[-1] if self.parent_stack else None

    def send(self,id, value, event_name):
        uix.socketio.emit("from_server", {'id': id, 'value': value, 'event_name': event_name}, room=self.sid)

    def queue_for_send(self, id, value, event_name):
        self.message_queue.append({'id': id, 'value': value, 'event_name': event_name})

    def flush_message_queue(self):
        for item in self.message_queue:            
            self.send(item['id'], item['value'], item['event_name'])
        self.message_queue = []

    def navigate(self, path):
        self.send("ait-uix", path, "navigate")

    def next_id(self):
        self._next_id += 1
        return self._next_id
