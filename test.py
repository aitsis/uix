
import uix
from uix.elements import div, button, container
uix.html.add_script("file", script =
"""
const onddivChange = (evt) => {
    console.log("onChange",evt);
    evtjson = JSON.stringify(evt);
    console.log("onChange",evtjson);
    clientEmit(evt.target.id,evtjson,"mychange");
};

""")
class ddiv(uix.Element):
    def __init__(self, value = None, id = None):
        super().__init__(value, id)
        self.tag = "div"
        
        self.has_content = True
    
    def get_client_handler_str(self, event_name):
        print("get_client_handler_str",event_name)
        if event_name in ["input","change"]:
            return f" on{event_name}=onddivChange(event)"
        else:
            return super().get_client_handler_str(event_name)



def on_btn_click(ctx, id, value):
    with ctx.elements["myEditor"]:
        button("Deneme")
    ctx.elements["myEditor"].update()


def on_change(ctx, id, value):
    print("change :", value)

def on_key_events(ctx, id, value):
    print("key_event :", value)

with div("",id="container") as __root:
    with ddiv("Hello World22", id ="myEditor") as myeditor:
        myeditor.attrs["contenteditable"] = True
        myeditor.value_name = "textContent"
        myeditor.on("input", on_change)
        myeditor.on("keyup", on_key_events)
        myeditor.on("keydown", on_key_events)
        myeditor.on("mychange", on_change)
    button("Click Me", id="button").on("click", on_btn_click)
    
#__root = button("Hello")

uix.start(ui = __root, config = {"debug":True})