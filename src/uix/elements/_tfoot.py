from ..core.element import Element

class tfoot(Element):
    def __init__(self,value = None, id = None,name = None):
        super().__init__(value, id = id)    
        self.tag = "tfoot"

title = "Table Footer"

description = '''
# tfoot(value,id = None)
1. Tablonun alt kısmı için kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | tfoot elementinin id'si                          |
    | value         | tfoot elementinin içeriği                       |
'''

sample = """
with table():
    with tfoot():
        text("Table Footer")
"""