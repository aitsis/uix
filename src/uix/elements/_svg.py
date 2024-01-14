from ..core.element import Element
print("Imported: svg")
class svg(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)
        self.tag = "svg"
    
    def viewbox(self, value):
        self.attrs["viewBox"] = value
        return self


title = "Svg"

description = '''
## svg(value,id = None)
1. Svg elementi. Html'deki svg elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Svg elementinin id'si                          |
| value         | Svg elementinin içeriği                       |
'''
