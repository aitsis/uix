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
