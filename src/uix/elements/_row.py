from ..core.element import Element
print("Imported: row")
class row(Element):
    def __init__(self,value:str = None, id:str = None):
        super().__init__(value = value, id = id)
        self.classes.append("row")



title = "Row"

description = '''
## row(value,id)
1. Row elementi. Temel olarak bir satırı temsil eder. İçerisindeki elemanları yan yana ekler.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Row elementinin id'si                          |
| value         | Row elementinin içeriği                       |
'''

sample = """
with row():
    button("Buton",id="btn1")
    button("Buton",id="btn2")
    button("Buton",id="btn3")
"""

