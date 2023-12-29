from ..core.element import Element
print("Imported: listitem")

class listitem(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id=id, value=value)
        self.tag = "li"
        self.value_name = "innerHTML"
        self.attrs["class"] = "list-item"
        
title = "List Item"
description = '''
Liste elemanı elementi. Sıralı liste elementine veya sırasız liste elementine eleman eklemek için kullanılır.
value : Liste elemanının içeriği
id : Liste elemanının id'si
attributes : Liste elemanına ait attribute'lar
attrs["class"] : Liste elemanına ait class'lar. Varsayılan değer: list-item

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