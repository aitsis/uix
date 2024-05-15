from ..core.element import Element
print("Imported: summary")
class summary(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)
        self.tag = "summary"