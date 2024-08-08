import uix
from ..core.element import Element
print("Imported: dialog")

dialog_script = '''
    event_handlers["dialog-close"] = function(id, value, event_name){
        const dialog = document.getElementById(id);
        dialog.close();
    };

    event_handlers["dialog-show"] = function(id, value, event_name){
        close_on_outside = value;
        const dialog = document.getElementById(id);
        dialog.showModal();
        if (close_on_outside) {
            window.onclick = function(event) {
                if (event.target === dialog) {
                    dialog.close();
                }
            };
        }
    };

'''

dialog_css = '''
dialog {
    background: var(--background);
    color:var(--font-color);
    border-radius: 3px;
    border:1px solid var(--border-color);
}

::backdrop {
  background: black;
  opacity: 0.3;
}'''

class dialog(Element):
    def __init__(self,value:str = None,id:str = None, close_on_outside:bool = True):
        super().__init__(value, id = id)
        self.register_script("dialog_script", dialog_script)
        self.register_style("dialog_css", dialog_css)
        self.tag = "dialog"
        self.has_content = True
        self.close_on_outside = close_on_outside

    def show(self):
        self.session.send(self.id, self.close_on_outside, "dialog-show")
        return self

    def hide(self):
        self.session.send(self.id, self.close_on_outside, "dialog-close")
        return self
