from ..core.element import Element

class textarea(Element):
    def __init__(self, value = None , id = None, placeholder = None):
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
textarea(placeholder = "Bir şeyler yazın..."):
"""