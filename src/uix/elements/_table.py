from ..core.element import Element

class table(Element):
    def __init__(self,value = None, id = None):
        super().__init__(value, id = id)    
        self.tag = "table"

title = "Table"
description = '''
# table(value,id = None)
1. Table elementi. Html'deki table elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Table elementinin id'si                          |
    | value         | Table elementinin içeriği                       |
'''
sample = """
with table():
    with tr():
        with th():
            text("Başlık 1")
        with th():
            text("Başlık 2")
        with th():
            text("Başlık 3")
    with tr():
        with td():
            text("Değer 1")
        with td():
            text("Değer 2")
        with td():
            text("Değer 3")
"""
