from ..core.element import Element
print("Imported: div")
class div(Element):
    def __init__(self,value,id = None, autoBind=True):
        super().__init__(value, id = id, autoBind=autoBind)
        