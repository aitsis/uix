from ..core.element import Element
print("Imported: label")

class label(Element):
    def __init__(self,value:str= None,id:str = None, tabindex:int = -1, usefor:str = None):
        super().__init__(value, id = id)
        self.classes.append("label")
        self.usefor = usefor
        self.tag = "label"
        self.attrs["tabindex"] = tabindex
        self.attrs["for"] = usefor
        self.has_content = True

title = "Label"

description = '''
# label(value,id,tabindex = -1,usefor = None)
1. Label elementi. Bir input elementine ait label elementi için kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Labelin id'si                          |
| value         | Label içeriği                       |
| tabindex      | Labelin tabindex'i. Varsayılan değer: -1. Değer -1 ise tab ile focuslanamaz. |
| usefor        | Labelin kullanıldığı input elementinin id'si |
'''
sample = """
    label("This Text is a Label!").style("font-size","20px")
        
"""