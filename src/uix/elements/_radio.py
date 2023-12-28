from ..core.element import Element

class radio(Element):
    def __init__(self,id = None,value = None,name = None):
        super().__init__(value, id = id)
        self.tag = "input"
        self.attrs["type"] = "radio"
        self.attrs["name"] = name

title = "radio"
description = """
Temel HTML radio elementi.
value: radio elementinin değeri.
id: radio elementinin id'si.
name: radio elementinin bağlı olduğu grubun adı.
"""

sample = """
with Form() as f:
    Radio(name = "group1"):
    Radio(name = "group1"):
    Radio(name = "group1"):

"""