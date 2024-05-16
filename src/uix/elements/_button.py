from uuid import uuid4
from ..core.element import Element
print("Imported: Button")
class button(Element):
    def __init__(self,value:str,id:str = None, type:str='button', formID:str=None, disabled:bool=False):
        super().__init__(value, id = id)
        self.tag = "button"
        self.attrs["type"] = type
        self.value_name = "innerHTML"
        self.disabled = disabled

        if formID is not None:
            self.attrs["form"] = formID

        if self.disabled:
            self.attrs["disabled"] = "disabled"
