from ..core.element import Element
print("Imported: input")
class input(Element):
    def __init__(self,value:str = None, id:str = None, type: str='text', name:str=None, placeholder:str="",
                 required:bool=False, list:str=None, autocomplete:bool=True, min:str=None, max:str=None):
        super().__init__(value, id = id)
        self.tag = "input"
        self.value_name = "value"
        self.has_content = False

        if type is not None:
            self.attrs["type"] = type
        
        if placeholder is not None:
            self.attrs["placeholder"] = placeholder

        if name is not None:
            self.attrs["name"] = name

        if required:
            self.attrs["required"] = "required"
        
        if list is not None:
            self.attrs["list"] = list

        if autocomplete == False:
            self.attrs["autocomplete"] = "off"
        
        if min is not None:
            self.attrs["min"] = min
        
        if max is not None:
            self.attrs["max"] = max

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self