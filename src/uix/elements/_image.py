from ..core.element import Element
print("Imported: image")
class image(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)
        self.tag = "img"
        self.value_name = "src"
        self.has_content = False

title = "Image"

description = '''
## image(value,id = None)
1. Html'deki img elementine karşılık gelir. Sayfada görüntülenmesi istenen resimler için kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Image elementinin id'si                          |
| value         | Image elementinin src'si                       |
'''

sample = """
def image_example():
    image_url = "https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png"
    main = image(image_url).cls("image")
    return main
"""
