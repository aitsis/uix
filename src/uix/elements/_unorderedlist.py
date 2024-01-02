from ..core.element import Element
print("Imported: unorderedlist")
class unorderedlist(Element):
    def __init__(self,value = None, id = None, role = None):
        super().__init__(value = value, id = id)
        self.tag = "ul"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["role"] = role

title = "Unorderedlist"
description = '''
# unorderedlist(value,id,role)
1. Temel unorderedlist elementi listitem elementleri ile kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | unorderedlistin id'si                          |
    | value         | unorderedlistin içeriği                       |
    | role          | unorderedlistin rolü |
'''

sample = """
def unorderedlist_example():
    with unorderedlist("").style("margin","auto").style("display","block"):
        listitem("Item 1")
        listitem("Item 2")
        listitem("Item 3")
"""