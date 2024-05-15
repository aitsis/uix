from ..core.element import Element
print("Imported: label")

class label(Element):
    def __init__(self,value:str= None,id:str = None, tabindex:int = -1, usefor:str = None):
        super().__init__(value, id = id)
        self.classes.append("label")
        self.usefor = usefor
        self.tag = "label"
        self.attrs["tabindex"] = tabindex
        self.attrs["for"] = usefor
        self.has_content = True
        self.value_name = "innerHTML"