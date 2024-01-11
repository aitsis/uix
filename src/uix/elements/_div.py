from ..core.element import Element
print("Imported: div")
class div(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)

title = "Div"

description = '''
## div(value,id = None)
1. Div elementi. Html'deki div elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Div elementinin id'si                          |
| value         | Div elementinin içeriği                       |
'''

sample = """
with div(''):
    text("Div")
"""
        