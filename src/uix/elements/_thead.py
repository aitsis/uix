from ..core.element import Element

class thead(Element):
    def __init__(self,value = None, id = None, name = None):
        super().__init__(value, id = id)    
        self.tag = "thead"

title = "Table Head"

description = '''
# thead(value,id = None)
1. Tablonun başlık kısmı. Tablonun içerisine başlık eklemek için kullanılır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | thead elementinin id'si                          |
    | value         | thead elementinin içeriği                       |
'''

sample = """
with table():
    with thead():
        with tr():
            with th():
                text("Name")
            with th():
                text("Surname")
"""