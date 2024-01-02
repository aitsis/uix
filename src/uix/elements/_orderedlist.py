from ..core.element import Element
print("Imported: Ordered List")

class orderedlist(Element):
    def __init__(self, value=None, id=None):
        super().__init__(value=value, id=id)
        self.tag = "ol"
        self.value_name = "innerHTML"
        self.has_content = True
        
title = "Ordered List"

description = '''
# orderedlist(value,id)
1. Sıralı liste elementi. Listeye eleman eklemek için listitem elementi kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Sıralı Listenin id'si                          |
    | value         | Liste içeriği                       |
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