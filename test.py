
import uix
from uix.elements import container, image, button, text
from uix.core.session import context

def disable(context, id, value):
    context.elements["my-button"].set_attr("disabled", True)

def enable(context, id, value):
    context.elements["my-button"].set_attr("disabled", False)


def components():
    if context.session.paths[1] == "view1":
        return view1()
    elif context.session.paths[1] == "view2":
        return view2()
    
    with container() as main:
        button("Click me Components", id="my-button")
        text("Hello world")
    return main



def view1():
    with container() as main:
        button("Click me 1", id="my-button")
        text(context.session.args.get("name", "No name"))
        text(context.session.args.get("email", "No name"))

        button("Disable", id="disable-btn").on("click", disable)
        button("Enable", id="enable-btn").on("click", enable)
    return main

def view2():
    with container() as main:
        button("Click me 2", id="my-button")
        text(context.session.args.get("name", "No name"))
        button("Disable", id="disable-btn").on("click", disable)
        button("Enable", id="enable-btn").on("click", enable)
    return main


def _root():
    with container() as main:
        if context.session is not None:
            print("Session:", context.session.args)
            print("Paths:", context.session.paths)
            print("Cookies:", context.session.cookies)

        paths = context.session.paths
        print("Paths:", paths)
        if len(paths) > 0:
            if paths[0] == "components":
                return components()
    return main

uix.start(ui = _root, config = {"debug":True})