from ..core.element import Element
print("Imported: footer")

class footer(Element):
    def __init__(self,value:str= None, id:str = None):
        super().__init__(value=value, id = id)
        self.tag = "footer"


title = "Footer"

description = '''
# footer(value,id = None)
1. Footer elementi. Html footer elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır. Sayfanın en altında yer alır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Footer elementinin id'si                          |
| value         | Footer elementinin içeriği                       |
'''

sample = """
    with page("") as footer_example:
        with header("",):
            text("Header Example")
        with main("",):
            text("Main Example")
        with footer("",):
            text("Footer Example")"""