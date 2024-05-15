from ..core.element import Element
print("Imported: Ordered List")

class orderedlist(Element):
    def __init__(self, value:str=None, id:str=None):
        super().__init__(value=value, id=id)
        self.tag = "ol"
        self.value_name = "innerHTML"
        self.has_content = True