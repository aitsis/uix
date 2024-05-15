from ..core.element import Element
print("Imported: unorderedlist")
class unorderedlist(Element):
    def __init__(self,value:str = None, id:str = None, role:str = None):
        super().__init__(value = value, id = id)
        self.tag = "ul"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["role"] = role