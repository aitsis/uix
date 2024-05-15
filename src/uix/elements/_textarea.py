from ..core.element import Element

class textarea(Element):
    def __init__(self, value:str = None , id:str = None, placeholder:str = None, required:bool = False):
        super().__init__(value, id = id)
        self.tag = "textarea"
        self.attrs["placeholder"] = placeholder
        self.classes.append("textarea")
        if required is not None:
            self.attrs["required"] = "required"

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self