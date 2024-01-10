from ..core.element import Element
print("Imported: Check")
class check(Element):
    def __init__(self, value = None, checked = False, id = None, disabled = False ):
        super().__init__(value, id = id)
        self.tag = "input"
        self.attrs["type"] = "checkbox"
        self.value_name = "checked"
        self.classes.append("form-check-input")
        self.has_content = False
        self.attrs["disabled"] = disabled

title = "Check"

description = """

# check(value,id,checked,disabled)
1. Checkbox bir input elementidir.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Check elementinin id'si                           |
    | value         | Check elementinin içeriği                        |
    | checked       | Check'in seçili olup olmadığı                     |
    | disabled      | Check'in etkinliğini kapatır.                     |
"""
sample = """
def check_example():
    main = check("", id="check").on("click", on_click)
    test = div("test", "test")
    return main

def on_click(ctx, id, value):
    print("Clicked", id, value)
    if value == False:
        ctx.elements["test"].value = "Unchecked!"
    else:
        ctx.elements["test"].value = "Checked!"
    ctx.elements["test"].update()
"""