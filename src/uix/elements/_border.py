from ..core.element import Element
print("Imported: border")
class border(Element):
    def __init__(self,value,id = None):
        super().__init__(value, id = id)
        self.classes.append("border")

title = "Border"

description = '''
Border elementi. Kenarında 1px kalınlığında çizgi bulunan bir div oluşturur. İçerisine elemanlar eklenerek kullanılır.
id= Border elementinin id'si
value= Border elementinin içeriği
'''

sample = """
with border(''):
    with div(''):
        text("Border")    
"""