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
def table_example():
    with table() as main:
        with thead():
            with tr():
                th(value="Name")
                th(value="Surname")
                th(value="Age")
        with tbody():
            with tr():
                td(value="John")
                td(value="Doe")
                td(value="32")
            with tr():
                td(value="Jane")
                td(value="Doe")
                td(value="31")
        with tfoot():
            with tr():
                td(value="John")
                td(value="Doe")
                td(value="32")
    return main
"""
