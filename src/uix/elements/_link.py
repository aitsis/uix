from ..core.element import Element

print("Imported: link")

class link(Element):
    def __init__(self,value:str,id:str = None, href:str = None, title:str="", target:str=""):
        super().__init__(value, id = id)
        self.tag = "a"
        self.value_name ="innerHTML"
        self.attrs["href"] = href
        self.attrs["title"] = title
        self.attrs["target"] = target