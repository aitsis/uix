from ..core.element import Element

class textarea(Element):
    def __init__(self, value:str = None , id:str = None, placeholder:str = None):
        super().__init__(value, id = id)
        self.tag = "textarea"
        self.attrs["placeholder"] = placeholder
        self.classes.append("textarea")

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self
    

title = "Textarea"
description = """
# textarea(value,id,placeholder)
1. Temel textarea elementi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Textarea elementinin id'si                          |
| value         | Textarea elementinin içeriği                       |
| placeholder   | Textarea elementinin placeholder değeri            |
"""
sample = """
def textarea_example():
    main = textarea("","text", placeholder="Selam").on("input", on_change)
    div(id="test", value="Selam")
    return main

def on_change(ctx, id, value):
    print("Changed", id, value)
    ctx.elements["test"].value = value
    ctx.elements["test"].update()

"""