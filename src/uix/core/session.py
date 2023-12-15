from .htmlgen import HTMLGen
class Session:
    def __init__(self,sid,ui,app):
        self.sid = sid
        self.app = app
        self.ui_root = ui
        self.index = HTMLGen()
        self.parent_stack = []
        self.elements = {}
        self.message_queue = []

    def clientHandler(self, data):
        print(data)
        if data["id"] == "myapp":
            if data["value"] == "init":                
                print("Client Initialized")
                ui = self.ui_root()
                ui.bind(self.sid)
                html = ui.render()
                print(html)
                self.send("myapp", html, "init-content")
                self.flush_message_queue()
        else:
            if id in self.elements:
                elm = self.elements[id]
                if elm is not None:            
                    if event_name in elm.events:
                        elm.events[event_name](self, id, value)
    
    def push_parent(self, parent):
        self.parent_stack.append(parent)

    def pop_parent(self):
        return self.parent_stack.pop()

    def current_parent(self):
        return self.parent_stack[-1] if self.parent_stack else None

    def send(self,id, value, event_name):
        self.app.server.emit("from_server", {'id': id, 'value': value, 'event_name': event_name}, room=self.sid)

    def queue_for_send(self, id, value, event_name):
        self.message_queue.append({'id': id, 'value': value, 'event_name': event_name})

    def flush_message_queue(self):
        for item in self.message_queue:            
            self.send(item['id'], item['value'], item['event_name'])
        self.message_queue = []

    def navigate(self, path):
        self.send("myapp", path, "navigate")
