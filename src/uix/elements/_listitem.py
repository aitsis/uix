from ..core.element import Element
print("Imported: listitem")

class listitem(Element):
    def __init__(self,value=None, id=None ):
        super().__init__(value=value, id=id)
        self.tag = "li"
        self.value_name = "innerHTML"
        self.attrs["class"] = "list-item"
        
title = "List Item"

description = '''
# listitem(value,id)
1. Liste elemanı elementi. Sıralı liste elementine veya sırasız liste elementine eleman eklemek için kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Liste elemanının id'si                          |
    | value         | Liste elemanının içeriği                       |
    | attributes    | Liste elemanına ait attribute'lar              |
    | attrs["class"]| Liste elemanına ait class'lar. Varsayılan değer: list-item |


'''
sample = """
    with parent:
        with orderedlist("Liste",id="list1"):
            listitem("Liste elemanı 1")
            listitem("Liste elemanı 2")
            listitem("Liste elemanı 3")
            listitem("Liste elemanı 4")
            listitem("Liste elemanı 5")
 """