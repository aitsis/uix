import uix
from ..core.element import Element
print("Imported: md")
uix.html.add_header_item("md", 
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/showdown/2.0.3/showdown.min.js"></script>')
uix.html.add_script("md", beforeMain = False, script =
'''
    var converter = new showdown.Converter();
    event_handlers["md-change-md"] = function(id, value, event_name){
        document.getElementById(id).innerHTML = converter.makeHtml(value);
    }
''')
class md(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)

    def bind(self, session, only_children=False):
        if self.id is None:
            self.id = "md_" + str(session.next_id())
        super().bind(session, only_children)
        self.session.queue_for_send(self.id, self.value, "md-change-md")
    
    def send_value(self, value):
        self.session.send(self.id, value, "md-change-md")

    