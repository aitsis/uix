from ..core.element import Element
print("Imported: slider")

class slider(Element):
    def __init__(self, value:str=None, id:str=None, min:int=0, max:int=100, step:int=1, list:str=None):
        super().__init__(value=value, id=id)
        self.min = min
        self.max = max
        self.step = step
        self.tag = "input"
        self.value_name = "value"
        self.has_content = False
        self.attrs["type"] = "range"
        self.attrs["min"] = self.min
        self.attrs["max"] = self.max
        self.attrs["step"] = self.step
        if list is not None:
            self.attrs["list"] = list
        
    def disable(self):
        self.attributes["disabled"] = "disabled"
        return self