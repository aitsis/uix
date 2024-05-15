from ..core.element import Element
print("Imported: page")

class page(Element):
    def __init__(self,value:str,id:str = None):
        super().__init__(value, id = id)
        self.classes.append("page")

