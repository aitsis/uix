from ..core.element import Element
print("Imported: main")

class main(Element):
    def __init__(self,value:str = None, id:str = None):
        super().__init__(value=value, id = id)
        self.tag = "main"


title = "Main"

description = '''
## main(value,id = None)

1. Main elementi. Html main elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Main elementinin id'si                          |

'''

sample = """
    with page("") as footer_example:
        with header("",):
            text("Header Example")
        with main("",):
            text("Main Example")
        with footer("",):
            text("Footer Example")
"""