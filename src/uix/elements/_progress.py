from ..core.element import Element
print("Imported: progress")
class progress(Element):
    def __init__(self,value = 0,id = None, max = 100):
        super().__init__(value, id = id)
        self.tag = "progress"
        self.max = max
        self.attrs["max"] = max