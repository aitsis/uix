from ..core.element import Element
print("Imported: Form")

enctypes = [
    "application/x-www-form-urlencoded",
    "multipart/form-data",
    "text/plain"
]
class form(Element):
    def __init__(
        self,
        value: str=None,
        id: str=None,
        action:str=None,
        method:str=None,
        enctype=enctypes[0],
        ):
        super().__init__(value=value, id=id)
        self.tag = "form"
        if method is not None:
            self.attrs["method"] = method
        
        if enctype is not None:
            self.attrs["enctype"] = enctype
            
        if action is not None:
            self.attrs["action"] = action