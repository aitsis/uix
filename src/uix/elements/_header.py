from ..core.element import Element
print("Imported: header")

class header(Element):
    def __init__(self,value:str = None, id:str = None):
        super().__init__(value=value, id = id)
        self.tag = "header"
