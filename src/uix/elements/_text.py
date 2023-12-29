from ..core.element import Element
print("Imported: text")

class text(Element):
    def __init__(self,value,id = None):
        super().__init__(value, id = id)
        self.tag = "p"
        self.value_name = "innerHTML"

title = "Text"

description = '''
Text elementi. Html'deki p elementine karşılık gelir. Sayfada yazı göstermek için kullanılır.

id= Text elementinin id'si
value= Text elementinin içeriği
'''

sample = """
with parent():
    value = "Hello World"
    text(value=value)
"""