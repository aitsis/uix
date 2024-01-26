
import uix
from uix.elements import div, button, container, unorderedlist, listitem

def on_mouse_down(ctx, id, value):
    print("mouse down :",id,value)


def _root():
    main = div().on("mousedown",on_mouse_down).size(300,300).on("keydown",lambda ctx,id,value: print("keydown",id,value)).cls("border").attr("tabindex",0)
    return main


uix.start(ui = _root(), config = {"debug":True})