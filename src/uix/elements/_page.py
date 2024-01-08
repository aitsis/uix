from ..core.element import Element
print("Imported: page")

class page(Element):
    def __init__(self,value,id = None):
        super().__init__(value, id = id)
        self.classes.append("page")

title = "Page"

description = '''
# page(value,id)
1. Page elementi. İçi boş bir ana div oluşturur. Sıfırdan bir sayfa oluşturmak için kullanılabilir. İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Page elementinin id'si                          |
    | value         | Page elementinin içeriği                       |
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

