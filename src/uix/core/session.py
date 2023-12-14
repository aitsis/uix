from .htmlgen import HTMLGen
class Session:
    def __init__(self,sid,ui):
        self.sid = sid
        self.ui = ui
        self.cur_parent = None
        self.index = HTMLGen()
        self.parent_stack = []
        self.elements = {}

    def clientHandler(self, data):
        if data.id == "myapp":
            if data.value == "init":                
                print("Client Initialized")
                self.send("myapp", self.ui.render(), "init-content")
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
