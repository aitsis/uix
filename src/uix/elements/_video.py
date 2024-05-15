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