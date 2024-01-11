from ..core.element import Element
print("Imported: header")

class header(Element):
    def __init__(self,value:str = None, id:str = None):
        super().__init__(value=value, id = id)
        self.tag = "header"


title = "Header"

description = '''
## header(value,id = None)
1. Header elementi. Html header elementine karşılık gelir. İçerisine eklenen elemanlar, kullanıldığı divin en üstünde yer alır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Header elementinin id'si                          |
| value         | Header elementinin içeriği                       |
'''

sample = """
    with page("") as footer_example:
        with header("",):
            text("Header Example")
        with main("",):
            text("Main Example")
        with footer("",):
            text("Footer Example")"""
