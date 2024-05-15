from ..core.element import Element

class table(Element):
    def __init__(self,value:str,id:str = None):
        super().__init__(value, id = id)    
        self.tag = "table"
