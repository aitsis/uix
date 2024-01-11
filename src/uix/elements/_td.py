from ..core.element import Element

class td(Element):
    def __init__(self, value:str = None, id:str = None):
        super().__init__(value, id = id)    
        self.tag = "td"

title = "Table Data"
description = '''
## td(value,id = None)
1. Td elementi. Html'deki td elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Td elementinin id'si                          |
| value         | Td elementinin içeriği                       |
'''

sample = """
with table():
    with tbody():
        with tr():
            with td():
                text("Değer 1")
            with td():
                text("Değer 2")
            with td():
                text("Değer 3")
"""