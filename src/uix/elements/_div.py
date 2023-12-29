from ..core.element import Element
print("Imported: div")
class div(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)

title = "Div"

description = '''
Div elementi. Html'deki div elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.
id= Div elementinin id'si
value= Div elementinin içeriği
'''

sample = """
with div(''):
    text("Div")
"""
        