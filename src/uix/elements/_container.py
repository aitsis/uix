from ..core.element import Element
print("Imported: container")
class container(Element):
    def __init__(self,value:str ,id:str = None):
        super().__init__(value, id = id)
        self.classes.append("container")


title = "Container"

description = '''
# container(value,id = None)
1. Container elementi. İçerisine elemanlar eklenerek kullanılır. Eklenen elemanları yatayda ve dikeyde ortalar.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Container elementinin id'si                          |
| value         | Container elementinin içeriği                       |
'''

sample = """
    with container(""):
        text("Hello World")

"""
