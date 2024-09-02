from ..core.element import Element
print("Imported: Legend")
class legend(Element):
	def __init__(self,value:str = None,id:str = None):
		super().__init__(value, id = id)
		self.tag = "legend"