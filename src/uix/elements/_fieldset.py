from ..core.element import Element
print("Imported: Fieldset")
class fieldset(Element):
	def __init__(self,value:str = None,id:str = None, disabled:bool=False):
		super().__init__(value, id = id)
		self.tag = "fieldset"
		self.disabled = disabled
		self.classes.append("border")

		if self.disabled:
			self.attrs["disabled"] = "disabled"