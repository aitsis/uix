from ..core.element import Element

class radio(Element):
    def __init__(self,value:str = None, id:str = None,name:str = None):
        super().__init__(value, id = id)
        self.tag = "input"
        self.attrs["type"] = "radio"
        self.attrs["name"] = name