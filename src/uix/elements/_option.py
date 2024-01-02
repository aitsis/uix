from ..core.element import Element
print("Imported: option")
class option(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id,)
        self.tag = "option"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["value"] = value

    def selected(self):
        self.attrs["selected"] = "true"
        return self
    
    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self


title = "option"

description = '''
# option(value,id)
1. Temel option elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Option elementinin id'si                          |
    | value         | Option elementinin içeriği                       |
    | selected      | Optionun varsayılan olarak seçili olucak değeri tanımlar. |
    | disabled      | Optionun etkinliğini kapatır. |
'''

sample = """
with parent:
    option("value",id="option1")
"""