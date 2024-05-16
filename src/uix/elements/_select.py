from ..core.element import Element
print("Imported: select")
class select(Element):
    def __init__(self,value:str = None,id:str = None, disabled:bool=False):
        super().__init__(value=value, id=id)
        self.tag = "select"
        self.value_name = "value"
        self.has_content = True
        
        if disabled:
            self.attrs["disabled"] = "disabled"