from ..core.element import Element
print("Imported: page")

class page(Element):
    def __init__(self,value,id = None):
        super().__init__(value, id = id)
        self.classes.append("main")

title = "Page"

description = '''
Page elementi. İçi boş bir ana div oluşturur. İçerisine elemanlar eklenerek kullanılır.

id= Page elementinin id'si
value= Page elementinin içeriği
'''

sample = """
with page('') as page:
    with header("") as header_example:
        text("Header")
    with container("") as content:
        text("Content")
        
"""

