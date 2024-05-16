from ..core.element import Element
print("Imported: embed")

class embed(Element):
    def __init__(self, value:str=None, id:str=None, type:str=None, width:str=None, height:str=None):
        super().__init__(value = value, id=id)
        self.tag = "embed"
        self.value_name = "src"

        self.has_content = False

        if type is not None:
            self.attrs["type"] = type

        if width is not None:
            self.attrs["width"] = width

        if height is not None:
            self.attrs["height"] = height