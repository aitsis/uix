from ..core.element import Element

class td(Element):
    def __init__(self,id = None,value = None):
        super().__init__(value, id = id)    
        self.tag = "td"