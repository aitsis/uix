from ..core.element import Element

class th(Element):
    def __init__(self,value = None, id = None, name = None):
        super().__init__(value, id = id)    
        self.tag = "th"

title = "Table Header"

description = '''
# th(value,id = None)

1. Html'deki th elementine karşılık gelir. Tablo başlıkları için kullanılır.
    
        | attr          | desc                                              |
        | :------------ | :------------------------------------------------ |
        | id            | Th elementinin id'si                          |
        | value         | Th elementinin içeriği                       |
    '''

sample = """
with table():
    with tr():
        th("Header 1")
        th("Header 2")
        th("Header 3")
    with tr():
        td("Data 1")
        td("Data 2")
        td("Data 3")
    with tr():
        td("Data 4")
        td("Data 5")
        td("Data 6")
"""