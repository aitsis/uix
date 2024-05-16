from ..core.element import Element
print("Imported: Check")
class check(Element):
    def __init__(self, value: str = None, id: str = None, disabled:bool = False ):
        super().__init__(value, id = id)
        self.tag = "input"
        self.attrs["type"] = "checkbox"
        self.value_name = "checked"
        self.classes.append("form-check-input")
        self.has_content = False
        self.attrs["disabled"] = disabled