from ..core.element import Element

print("Imported: canvas")
class canvas(Element):
    def __init__(self,id:str = None, value = None, width: int= 300, height: int = 150):
        super().__init__(value = value, id = id)
        self.tag = "canvas"
        self.attrs["width"] = width
        self.attrs["height"] = height
        self.tag_name = None
        

title = "Canvas"

description = '''
## canvas(value,id = None)
1. Canvas elementi. Html'deki canvas elementine karşılık gelir. Genellikle Komponentler içinde kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Canvas elementinin id'si                          |
| width         | Canvas elementinin genişliği (piksel olarak)      |
| height        | Canvas elementinin yüksekliği (piksel olarak)     |
'''

sample = """
canvas1 = canvas():    
"""