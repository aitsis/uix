
import uix
from uix.elements import container, border
# Asenkron Attribute okuma yöntemi.
# İleride geliştirilecek ve daha kolay kullanılabilir hale getirilecek sistem için alt yapı.
def on_get_attr(ctx,id,value):
    print("clientHeight : ",value)
    ctx.elements["div2"].set_style("height",str(value)+"px")

def on_click(ctx,id,value):
    ctx.elements["div1"].get_attr("clientHeight",on_get_attr)

def _root():
    with container()as main:
        border(id="div1").size("100%",100).on("click",on_click)
        border(id="div2")
    return main

uix.start(ui = _root(), config = {"debug":True})