from ..core.element import Element

class tr(Element):
    def __init__(self,value = None, id = None,name = None):
        super().__init__(value, id = id)    
        self.tag = "tr"

title = "Table Row"

description = '''
# tr(value,id = None)
1. Html'deki tr elementine karşılık gelir. Tablo içerisinde satır oluşturmak için kullanılır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Tr elementinin id'si                          |
    | value         | Tr elementinin içeriği                       |
'''

sample = """
with table():
    with tr():
        text("Tr")
"""