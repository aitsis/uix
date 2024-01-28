from ..core.element import Element
print("Imported: row")
class row(Element):
    def __init__(self,value:str = None, id:str = None):
        super().__init__(value = value, id = id)
        self.classes.append("row")

    def center(self):
        self.styles["justify-content"] = "center"
        return self
    
    def left(self):
        self.styles["justify-content"] = "flex-start"
        return self
    
    def right(self):
        self.styles["justify-content"] = "flex-end"
        return self
    
title = "Row"

description = '''
## row(value,id)
1. Row elementi. Temel olarak bir satırı temsil eder. İçerisindeki elemanları yan yana ekler.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Row elementinin id'si                          |
| value         | Row elementinin içeriği                       |

## Row Elementi Fonksiyonları

| Fonksiyon     | Açıklama                                          |
| :------------ | :------------------------------------------------ |
| center()      | Row elementinin elemanlarını ortalar.            |
| left()        | Row elementinin elemanlarını sola yaslar.        |
| right()       | Row elementinin elemanlarını sağa yaslar.        |

'''

sample = """
with row():
    button("Buton",id="btn1")
    button("Buton",id="btn2")
    button("Buton",id="btn3")
"""

