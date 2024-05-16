from ..core.element import Element
print("Imported: col")
class col(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)
        self.classes.append("col")

    def align(self, align):
        self.styles["justify-content"] = align
        return self