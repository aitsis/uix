from ..core.element import Element
print("Imported: element")

class datalist(Element):
    def __init__(self, value: str=None, id:str =None):
        super().__init__(value, id=id)
        self.tag = "datalist"
        self.value_name = "innerHTML"
        self.has_content = True
