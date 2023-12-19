
import uix
from copy import deepcopy

class Context:
    def __init__(self, session, element):
        self.session = session
        self.element = element
        self.elements = session.elements
        self.data = {}

class Session:
    def __init__(self,sid):
        self.sid = sid
        self.ui_root = None
        self._next_id = 0
        self.elements = {}
        self.message_queue = []
        self.context = Context(self, None)

    def clientHandler(self, data):
        id = data["id"]
        if id == "myapp":
            if data["value"] == "init":                
                print("Client Initialized")
                if( uix.app.ui_root is not None):
                    self.ui_root = deepcopy(uix.app.ui_root)
                    self.ui_root.bind(self)
                    html = self.ui_root.render()
                    self.send("myapp", html, "init-content")
                    self.flush_message_queue()
                else:
                    print("No UI Root")
        else:
            event_name = data["event_name"]
            value = data["value"]
            if id in self.elements:
                elm = self.elements[id]
                if elm is not None:            
                    if event_name in elm.events:
                        self.context.element = elm
                        elm.events[event_name](self.context, id, value)
    
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
        self.send("myapp", path, "navigate")

    def next_id(self):
        self._next_id += 1
        return self._next_id
