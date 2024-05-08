from uuid import uuid4
from .session import Session, context
import uix
class Element:
    def __init__(self, value = None, id = None):
        self.session = context.session
        self.tag = "div"
        self.id = id
        self._value = value
        self.children = []
        self.events = {}
        self.styles = {}
        self.classes = []
        self.attrs = {}
        self.parent = None
        self.old_parent = None
        self.value_name = "value"
        self.has_content = True
        
        if self.session.ui_root is None:
            self.session.ui_root = self

        self.parent = self.session.ui_parent
        if self.parent is not None:
            self.parent.children.append(self)
    
        if self.id is not None:
            self.session.elements[self.id] = self

    def _init(self):
        self.init()
        for child in self.children:
            child._init()

    def init(self):
        pass
    # WITH ENTRY - EXIT -------------------------------------------------------------------------------
    def enter(self):
        self.old_parent = self.session.ui_parent
        self.session.ui_parent = self
        self.children = []
        return self
    
    def exit(self):
        self.session.ui_parent = self.old_parent
    
    def __enter__(self):
        return self.enter()
    
    def __exit__(self, type, value, traceback):
        self.exit()

    def __str__(self):
        return self.render()
    
    # RUNTIME UPDATE ELEMENT ------------------------------------------------------------------------
    def update(self, content = None):
        if content is not None:
            with self:
                content()
        self.session.send(self.id, self.render(), "init-content")
        self.session.flush_message_queue()

    # VALUE -----------------------------------------------------------------------------------------
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.send_value(value)

    def send_value(self, value):
        if(self.id is None):
            self.id = str(uuid4())
            self.session.elements[self.id] = self
        self.session.send(self.id, value, "change-"+self.value_name)

    def set_value(self, value):
        self.value = value

    def set_timeout(self, time, callback):
        self.events["timeout"] = callback
        self.session.send(self.id, time, "set-timeout")
    # RUNTIME JAVASCRIPT -------------------------------------------------------------------------------  
    def toggle_class(self, class_name):
        self.session.send(self.id, class_name, "toggle-class")

    def add_class(self, class_name):
        self.session.send(self.id, class_name, "add-class")

    def remove_class(self, class_name):
        self.session.send(self.id, class_name, "remove-class")

    def set_attr(self, attr_name, attr_value):
        self.attrs[attr_name] = attr_value
        self.session.send(self.id, attr_value, "change-"+attr_name)
    
    def get_attr(self, attr_name,callback):
        self.events["get-"+attr_name] = callback
        self.session.send(self.id, None, "get-"+attr_name)
        
    def set_style(self, attr_name, attr_value):
        self.styles[attr_name] = attr_value
        self.session.send(self.id, attr_value, "set-"+attr_name)

    def focus(self):
        self.session.send(self.id, None, "focus")

    # RENDER -----------------------------------------------------------------------------------------
    def cls(self, class_names):
        if isinstance(class_names, str):
            classes = class_names.split()
            self.classes.extend([cls.strip() for cls in classes])
        return self

    def style(self,style,value = None):
        if value is None: 
            self.styles[style] = None
        else:
            self.styles[style] = value
        return self
    
    def size(self, width = None, height = None):
        if width is not None:
            if type(width) is int:
                width = str(width) + "px"
            self.styles["width"] = width
        if height is not None:       
            if type(height) is int:
                height = str(height) + "px"
            self.styles["height"] = height
        return self
    
    def attr(self, attr_name, attr_value):
        self.attrs[attr_name]=attr_value
        return self

    def bg(self, color):
        self.styles["background-color"] = color
        return self
    def align(self, align):
        self.styles["text-align"] = align
        return self
    # PYTHON EVENTS ----------------------------------------------------------------------------------
    def on(self,event_name,action):
        if(self.id is None):
            self.id = str(uuid4())
            self.session.elements[self.id] = self
        self.events[event_name] = action
        return self

    # JAVASCRIPT EMIT --------------------------------------------------------------------------------
    def get_client_handler_str(self, event_name):
        mouse_events = ["mousedown","mouseup","mouseover","mousemove","mouseout","mouseenter","mouseleave"]
        keyboard_events = ["keydown","keyup","keypress"]
        if event_name in mouse_events:
            return f" on{event_name}='mouseEvent(event)'"
        elif event_name in keyboard_events:
            return f" on{event_name}='keyboardEvent(event)'"
        else:
            return f" on{event_name}='clientEmit(this.id,this.{self.value_name},\"{event_name}\")'"

    # RENDER -----------------------------------------------------------------------------------------
    def render(self):
        str = f"<{self.tag}"
        if self.id is not None:
            str += f" id='{self.id}'"
        class_str = " ".join(self.classes)
        if(len(class_str) > 0):
            str += f" class='{class_str}'"
        if(len(self.styles) > 0):
            style_str = " style='"
            for style_name, style_value in self.styles.items():
                if style_value is None:
                    style_str += style_name
                else:
                    style_str += f" {style_name}:{style_value};"
            str += style_str + "'"
        for attr_name, attr_value in self.attrs.items():
            if isinstance(attr_value, bool):
                if attr_value:
                    str += f" {attr_name}"
            else:
                str += f" {attr_name}='{attr_value}'"
        for event_name, action in self.events.items():
            str += self.get_client_handler_str(event_name)
        if self.has_content:
            str +=">"
            str +=f"{self.value if self.value is not None and self.value_name is not None else ''}"
            for child in self.children:
                str += child.render()
            str += f"</{self.tag}>"
        else:
            if self.value is not None:
                if(self.value_name is not None):
                    if isinstance(self.value, bool):
                        if self.value:
                            str += f" {self.value_name}"
                    else:
                        str +=f' {self.value_name} ="{self.value}"'
            str += "/>"
        return str