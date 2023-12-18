from ..core.element import Element
print("Imported: border")
class border(Element):
    def __init__(self,value,id = None):
        super().__init__(value, id = id)
        self.classes.append("border")