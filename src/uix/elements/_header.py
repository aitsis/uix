from ..core.element import Element
print("Imported: header")

class header(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)
        self.tag = "header"


title = "Header"
description = '''
Header elementi. Html header elementine karşılık gelir. İçerisine eklenen elemanlar, kullanıldığı divin en üstünde yer alır.

id= Header elementinin id'si
value= Header elementinin içeriği
'''
sample = """
    with page("") as page:
        with header(""):
            text("Header")

        with div("") as main:
            text("Main")"""

