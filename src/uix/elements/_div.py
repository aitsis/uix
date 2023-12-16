from ..core.element import Element
print("Imported: div")
class div(Element):
    def __init__(self,value,id = None):
        super().__init__(value, id = id)
        