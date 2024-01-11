from ..core.element import Element

class tbody(Element):
    def __init__(self,value:str = None, id:str = None,name:str = None):
        super().__init__(value, id = id)    
        self.tag = "tbody"


title = "Table Body"
description = '''
## tbody(value,id = None)
1. Tbody elementi. Html'deki tbody elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Tbody elementinin id'si                          |
| value         | Tbody elementinin içeriği                       |
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