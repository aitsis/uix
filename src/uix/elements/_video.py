from ..core.element import Element

print("Imported: video")

class video(Element):
     def __init__(self, id=None, value=None,loop="true", autoplay="true", muted="true", src=None):
        super().__init__(id=id, value=value)
    
        if src is not None:
            self.attrs["src"] = src

        self.tag = "video"
        self.has_content = True
        self.attrs["loop"] = loop
        self.attrs["autoplay"] = autoplay
        self.attrs["playsinline"] = "true"
        self.attrs["muted"] = muted

title = "Video"

description = '''
    Video elementi. Html'deki video elementine karşılık gelir. İçerisine source elementleri eklenerek kullanılır.
    id= Video elementinin id'si
    loop= Video elementinin sürekli oynatılması
    autoplay= Video elementinin otomatik oynatılması
    muted= Video elementinin sesinin kapatılması
    src= Video elementinin src'si, burası isteğe bağlıdır, direkt src ile kaynak belirtilebileceği gibi source elementleri ile de belirtilebilir.
'''

sample = """
## sample1
with video(""):
    value = "https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4"
    source(value, type="video/mp4")

## sample2
    video("",src="https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4")
"""

