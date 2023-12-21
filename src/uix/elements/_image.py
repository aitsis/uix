from ..core.element import Element
print("Imported: image")
class image(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)
        self.tag = "img"
        self.value_name = "src"
        self.has_content = False