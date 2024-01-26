from ..core.element import Element
print("Imported: span")
class span(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)
        self.tag = "span"

title = "Span"

description = '''
## span(value,id = None)
1. Span elementi. Html'deki span elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Span elementinin id'si                            |
| value         | Span elementinin içeriği                          |
'''

sample = """
with span(''):
    text("span içeriği")
"""
        