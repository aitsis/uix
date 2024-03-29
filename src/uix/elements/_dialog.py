import uix
from ..core.element import Element
print("Imported: dialog")

uix.html.add_script("dialog", script =
'''
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
    
''',beforeMain=False)

uix.html.add_css("dialog_css", style = '''
dialog {
    background: var(--background);
    color:var(--font-color);
    border-radius: 3px;
    border:1px solid var(--border-color);
}
        
::backdrop {
  background: black;
  opacity: 0.3;
}''')

class dialog(Element):
    def __init__(self,value:str = None,id:str = None, close_on_outside:bool = True):
        super().__init__(value, id = id)
        self.tag = "dialog"
        self.has_content = True
        self.close_on_outside = close_on_outside
    
    def show(self):
        self.session.send(self.id, self.close_on_outside, "dialog-show")
        return self
    
    def hide(self):
        self.session.send(self.id, self.close_on_outside, "dialog-close")
        return self

title = "Dialog"

description = '''
## dialog(value,id = None, is_clickable_anywhere = True)

1. Dialog elementi. Bir dialog penceresi açar.

| attr                  | desc                                              |
| :-------------------- | :------------------------------------------------ |
| id                    | Dialog elementinin id'si                          |
| value                 | Dialog elementinin içeriği                       |
| close_on_outside      | Dışarı tıklanınca kapanma özelliği               |
'''

sample = """
def dialog_example1():
    with dialog(id="dialog_example",close_on_outside=True) as dialog1:
        with container("",):
            text("Dialog Example 1")
            text("Click anywhere to close")
            button("Close").on("click", lambda ctx, id, value: dialog.hide(dialog1))
    button("Dialog 1").on("click", lambda ctx, id, value: dialog.show(dialog1))
    return dialog1

def dialog_example2():
    with dialog(id="dialog1", close_on_outside=False) as dialog2:
        with container("",):
            text("Dialog Example 2")
            text("Click the close button to close")
            button("Close").on("click", lambda ctx, id, value: dialog.hide(dialog2))
    button("Dialog 2").on("click", lambda ctx, id, value: dialog.show(dialog2))
    return dialog2

def dialog_example():
    dialog_example1()
    dialog_example2()
"""