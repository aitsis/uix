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
def listitem_example():
    with unorderedlist("", id="listitem_example"):
        listitem("List Item 1",id="listitem1")           
        listitem("List Item 11",id="listitem11")
        listitem("List Item 12",id="listitem12")
        listitem("List Item 13",id="listitem13")
        listitem("List Item 14",id="listitem14")
        listitem("List Item 15",id="listitem15")
        listitem("List Item 16",id="listitem16")
        listitem("List Item 17",id="listitem17")
        listitem("List Item 18",id="listitem18")
        listitem("List Item 19",id="listitem19")
        listitem("List Item 20",id="listitem20")
        listitem("List Item 21",id="listitem21")
 """