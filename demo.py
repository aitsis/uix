import uix
from uix.elements import div, button

def on_click(session, id, value):
    print("Clicked!", id, value, session.sid)
    session.elements[id].value = "Clicked!" + str(session.next_id())

def comp1():
    with div("A!",):
        with div("C!"):
            button("E!").on("click", on_click)

    with div("B!"):
        with div("D!"):
            div("F!")


with div("Hello World!") as main:
    with div("A!",):
        comp1()
        with div("C!"):
            button("E!").on("click", on_click)

    with div("B!"):
        with div("D!"):
            div("F!")


print(main.render())
uix.start(ui = main)
