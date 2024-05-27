from ..core.element import Element
print("Imported: option")
class option(Element):
    def __init__(self,value:str = None,id:str = None, text:str = None, label:str = None):
        super().__init__(value=text, id = id,)
        self.tag = "option"
        self.value_name = "innerHTML"
        self.has_content = True
        if value is None:
            self.attrs["value"] = text
        else:
            self.attrs["value"] = value

        if label is not None:
            self.attrs["label"] = label
            
    def selected(self,selected = True):
        self.attrs["selected"] = selected
        return self
    
    def disabled(self,disabled = True):
        self.attrs["disabled"] = disabled
        return self


title = "option"

description = '''
## option(value,id)
1. Temel option elementi.

| attr          | desc                                                      |
| :------------ | :------------------------------------------------------   |
| id            | Option elementinin id'si                                  |
| value         | Option elementinin içeriği                                |
| selected      | Optionun varsayılan olarak seçili olucak değeri tanımlar. |
| disabled      | Optionun etkinliğini kapatır.                             |
| label         | Optionun etiketini tanımlar.                              |
'''

sample = """
with parent:
    option("value",id="option1")
"""