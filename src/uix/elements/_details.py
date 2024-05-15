from ..core.element import Element
print("Imported: details")

class details(Element):
    def __init__(self,value:str = None, id:str = None, open:bool = False):
        super().__init__(value=value, id = id)
        self.tag = "details"
        if open is not None:
            self.attrs["open"] = open