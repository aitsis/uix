import uix
from uix.elements import div, button

def on_click(session, id, value):
    print("Clicked!", id, value, session.sid)
    session.elements["btn_1"].value = "Clicked!" + str(session.next_id())
    
with div("Hello World!") as main:
    with div("A!",):
        with div("C!"):
            button("E!").on("click", on_click)

    with div("B!"):
        with div("D!"):
            div("F!")


print(main.render())
uix.start(ui = main)
