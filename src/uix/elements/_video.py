from ..core.element import Element

print("Imported: video")

class video(Element):
     def __init__(self, value:str = None, id:str = None,loop: bool=True, autoplay: bool=True, muted: bool=True, src:str=None):
        super().__init__(value=value,id=id)
    
        if src is not None:
            self.attrs["src"] = src

        self.tag = "video"
        self.has_content = True
        self.attrs["loop"] = loop
        self.attrs["autoplay"] = autoplay
        self.attrs["playsinline"] = "true"
        self.attrs["muted"] = muted

title = "Video"

description = """
# video(id,loop,autoplay,muted)
1. Html'de video elementine karşılık gelir. İçerisine source elementleri eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Video elementinin id'si                          |
| loop          | Video elementinin sürekli oynatılması            |
| autoplay      | Video elementinin otomatik oynatılması           |
| muted         | Video elementinin sesinin kapatılması            |
"""

sample = """
## sample1
with video(""):
    value = "https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4"
    source(value, type="video/mp4")

## sample2
    video("",src="https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4")
"""

