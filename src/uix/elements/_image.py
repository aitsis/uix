import uix
from uuid import uuid4
from ..core.element import Element
from ..core.session import context
from PIL import Image
import io
print("Imported: image")
class image(Element):
    def __init__(self,value = None,id:str = None, no_cache = True):    
        super().__init__(value = value, id = id)
        self.no_cache = no_cache
        self.tag = "img"
        self.value_name = "src"
        self.has_content = False
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, Image.Image):
            self.has_png_image = True
            self._value = self.create_image_url(value)
        else:
            self.has_png_image = False
            self._value = value
            
        if self.id is not None:
            self.send_value(self._value)
        else:
            print("No id for image")
    
    def __del__(self):
        if self.has_png_image:
            uix.app.files[self.id] = None

    def create_image_url(self,img):
        if self.id is None:
            self.id = str(uuid4())
        temp_data = io.BytesIO()
        img.save(temp_data, format="png")
        temp_data.seek(0)
        uix.app.files[self.id] = {"data":temp_data.read(),"type":"image/png"}
        return "download/"+self.id + "?" + str(uuid4()) if self.no_cache else "download/"+self.id
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
