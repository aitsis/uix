from ..core.element import Element

class tfoot(Element):
    def __init__(self,id = None,value = None,name = None):
        super().__init__(value, id = id)    
        self.tag = "tfoot"