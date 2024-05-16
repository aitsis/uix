from ..core.element import Element
print("Imported: text")

class text(Element):
    def __init__(self,value:str,id:str = None):
        super().__init__(value, id = id)
        self.tag = "text"
        self.value_name = "innerHTML"