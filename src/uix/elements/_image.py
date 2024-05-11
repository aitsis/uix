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
        self.has_PIL_image = False

        if isinstance(value, Image.Image):
            self.has_PIL_image = True
            self._value = self._create_image_url(value)
        else:
            self.has_PIL_image = False
            self._value = value
        if(self.id is None):
            self.id = str(uuid4())
            self.session.elements[self.id] = self
        self.session.queue_for_send(self.id, self.value, "change-"+self.value_name)
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, Image.Image):
            self.has_PIL_image = True
            self._value = self._create_image_url(value)
        else:
            self.has_PIL_image = False
            self._value = value
        if(self.id is None):
            self.id = str(uuid4())
            self.session.elements[self.id] = self
        self.session.send(self.id, self.value, "change-"+self.value_name)
        
    def __del__(self):
        if self.has_PIL_image:
            uix.app.files[self.id] = None

    def _create_image_url(self,img):
        if self.id is None:
            self.id = str(uuid4())
        temp_data = io.BytesIO()
        img.save(temp_data, format="png")
        temp_data.seek(0)
        uix.app.files[self.id] = {"data":temp_data.read(),"type":"image/png"}
        return "/download/"+self.id + "?" + str(uuid4()) if self.no_cache else "download/"+self.id
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
    pil_image = create_image()
    with col().style("align-items: center;") as main:
        text("Static Image")
        main = image(image_url).cls("image")
        text("PIL Image")
        main = image(pil_image).cls("image")    
    return main


from PIL import Image, ImageDraw, ImageFilter
def create_image():
    def gradient_circle(draw, center, radius, color1, color2):
        for i in range(radius, 0, -1):
            color = (
                int(color1[0] + (color2[0] - color1[0]) * i / radius),
                int(color1[1] + (color2[1] - color1[1]) * i / radius),
                int(color1[2] + (color2[2] - color1[2]) * i / radius)
            )
            draw.ellipse((center[0] - i, center[1] - i, center[0] + i, center[1] + i), fill=color)

    img_size = 400
    image = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(image)

    # Draw a grid of gradient circles
    spacing = 80  # Space between centers of circles
    radius = 40
    for x in range(spacing, img_size, spacing):
        for y in range(spacing, img_size, spacing):
            gradient_circle(draw, (x, y), radius, (255, 0, 0), (255, 255, 0))

    # Apply a slight blur to smooth out the gradients
    image = image.filter(ImageFilter.GaussianBlur(2))
    return image
"""
