from ..core.element import Element
print("Imported: text")

class text(Element):
    def __init__(self,value:str,id:str = None):
        super().__init__(value, id = id)
        self.tag = "p"
        self.value_name = "innerHTML"

title = "Text"

description = '''
## text(value,id = None)
1. Html'deki p elementine karşılık gelir. Sayfada görüntülenmesi istenen yazılar için kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Text elementinin id'si                          |
| value         | Text elementinin içeriği                       |
'''

sample = """
with parent():
    value = "Hello World"
    text(value=value)
"""