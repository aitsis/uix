from ..core.element import Element
print("Imported: Ordered List")

class orderedlist(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id=id, value=value)
        self.tag = "ol"
        self.value_name = "innerHTML"
        self.has_content = True
        
title = "Ordered List"
description = '''
Sıralı liste elementi. Listeye eleman eklemek için listitem elementi kullanılır.
value : Liste içeriği
id : Sıralı Listenin id'si
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