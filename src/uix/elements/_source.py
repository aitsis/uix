from ..core.element import Element
print("Imported: source")

class source(Element):
    def __init__(self,value:str,id:str = None, media:str = None,type:str ="video/mp4"):
        super().__init__(value, id = id)
        self.tag = "source"
        self.value_name = "src"
        self.has_content = False
        self.attrs["media"] = media
        self.attrs["type"] = type



title = "Source"

description = '''
## source(value,id,media,type)
1. Source elementi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Source elementinin id'si                          |
| value         | Source elementinin src'si                       |
| media         | CSS'de normalde tanımlanacak herhangi bir geçerli medya sorgusunu kabul eder. |
| type          | Kaynak dosyanın MIME türü. Örneğin, video/mp4, video/webm veya video/ogg. |
'''


sample = """
with video():
    source(value="video.mp4")
    source(value="video.webm",type="video/webm")
    source(value="video.ogg",type="video/ogg")
"""
