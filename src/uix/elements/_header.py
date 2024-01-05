from ..core.element import Element
print("Imported: header")

class header(Element):
    def __init__(self,value = None, id = None):
        super().__init__(value=value, id = id)
        self.tag = "header"
        self.classes.append("header")


title = "Header"

description = '''
# header(value,id = None)
1. Header elementi. Html header elementine karşılık gelir. İçerisine eklenen elemanlar, kullanıldığı divin en üstünde yer alır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Header elementinin id'si                          |
    | value         | Header elementinin içeriği                       |
'''

sample = """
    with div("") as header_example:
        header_example.style("height","100%")
        with header("",):
            button("Home")"""
