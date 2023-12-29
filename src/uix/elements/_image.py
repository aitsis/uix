from ..core.element import Element
print("Imported: image")
class image(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)
        self.tag = "img"
        self.value_name = "src"
        self.has_content = False

title = "Image"

description = '''
Html'deki img elementine karşılık gelir. Sayfada görüntülenmesi istenen resimler için kullanılır.

id= Image elementinin id'si
value= Image elementinin src'si
'''

sample = """
with parent():
    value = "image.png"
    image(value)
"""
