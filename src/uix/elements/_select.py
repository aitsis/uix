from ..core.element import Element
print("Imported: select")
class select(Element):
    def __init__(self,value = None,id = None, disabled=False):
        super().__init__(value=value, id=id)
        self.tag = "select"
        self.value_name = "value"
        self.has_content = True
        
        if disabled:
            self.attrs["disabled"] = "disabled"

title = "select"
description = '''
Temel select elementi. Tek başına kullanılmaz. Option elementleri ile kullanılır.
value : Selectin içeriği
id : Selectin id'si
selected : Option değerlerinden hangisinin başlangıç değeri olucağını tanımlar.
disabled : Selectin etkinliğini kapatır.
'''
sample = """
 with select(""):
        option("Option 1")
        option("Option 2").selected()
        option("Option 3")  
"""