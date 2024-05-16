from ..core.element import Element
print("Imported: border")
class border(Element):
    def __init__(self, value:str = None, id:str = None):
        super().__init__(value = value, id = id)
        self.classes.append("border")