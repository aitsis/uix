from ..core.element import Element

class radio(Element):
    def __init__(self,value = None, id = None,name = None):
        super().__init__(value, id = id)
        self.tag = "input"
        self.attrs["type"] = "radio"
        self.attrs["name"] = name

title = "radio"

description = """
# radio(value,id,name)
1. Temel HTML radio elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | radio elementinin id'si                          |
    | value         | radio elementinin değeri                       |
    | name          | radio elementinin bağlı olduğu grubun adı       |
"""


sample = """
with Form() as f:
    Radio(name = "group1"):
    Radio(name = "group1"):
    Radio(name = "group1"):

"""