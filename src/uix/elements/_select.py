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
# select(value,id)
1. Temel select elementi. Tek başına kullanılmaz. Option elementleri ile kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Select elementinin id'si                          |
    | value         | Select elementinin içeriği                       |
    | selected      | Option değerlerinden hangisinin başlangıç değeri olucak tanımlar. |
    | disabled      | Selectin etkinliğini kapatır. |
'''

sample = """
 with select(""):
        option("Option 1")
        option("Option 2").selected()
        option("Option 3")  
"""