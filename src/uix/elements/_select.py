from ..core.element import Element
print("Imported: select")
class select(Element):
    def __init__(self,value:str = None,id:str = None, disabled:bool=False):
        super().__init__(value=value, id=id)
        self.tag = "select"
        self.value_name = "value"
        self.has_content = True
        
        if disabled:
            self.attrs["disabled"] = "disabled"

title = "Select"

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
def on_change(ctx,id, value):
    ctx.elements["output"].value = value

def select_option_example():
    with select("Option 3", "mySelect").on("change",on_change):
        option("Option 1")
        option("Option 2").selected()
        option("Option 3")
    text("", id="output")         
"""