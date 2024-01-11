from ..core.element import Element
print("Imported: Ordered List")

class orderedlist(Element):
    def __init__(self, value:str=None, id:str=None):
        super().__init__(value=value, id=id)
        self.tag = "ol"
        self.value_name = "innerHTML"
        self.has_content = True
        
title = "Ordered List"

description = '''
## orderedlist(value,id)
1. Sıralı liste elementi. Listeye eleman eklemek için listitem elementi kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Sıralı Listenin id'si                          |
| value         | Liste içeriği                       |
'''
sample = """
def orderedlist_listitem_example():
    with orderedlist(id="myList"):
        listitem(value="Item 1")   
        listitem(value="Item 2")        
        listitem(value="Item 3")
 """