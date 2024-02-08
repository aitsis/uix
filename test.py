
import uix
from uix.elements import container, image, button
from uix.core.session import context

def _root():
    with container() as main:
        if context.session is not None:
            print("Session:", context.session.args)
            print("Paths:", context.session.paths)
            print("Cookies:", context.session.cookies)
        image("https://via.placeholder.com/150")
        button(f"Click me {context.session.args['user'][0]}", id="my-button")
    return main

uix.start(ui = _root, config = {"debug":True})