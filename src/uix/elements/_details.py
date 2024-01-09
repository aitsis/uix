from ..core.element import Element
print("Imported: details")
class details(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)
        self.tag = "details"