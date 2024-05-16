from ..core.element import Element
print("Imported: listitem")
class listitem(Element):
    def __init__(self,value:str=None, id:str=None ):
        super().__init__(value=value, id=id)
        self.tag = "li"
        self.value_name = "innerHTML"
        self.attrs["class"] = "list-item"