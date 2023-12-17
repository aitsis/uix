import uix
from uix.elements import div, button
counter = 0
def next_counter():
    global counter
    counter = counter + 1
    return counter

def on_click(session, id, value):
    session.elements[id].value = "Clicked!" + str(next_counter())

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
