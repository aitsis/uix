from ..core.element import Element
print("Imported: element")

class datalist(Element):
    def __init__(self, value: str=None, id:str =None):
        super().__init__(value, id=id)
        self.tag = "datalist"
        self.value_name = "innerHTML"
        self.has_content = True

title = "Datalist"
description = '''
## datalist(value,id = "myDataList")
1. Datalist elementi. Html'deki datalist elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Datalist elementinin id'si                          |
| value         | Datalist elementinin içeriği                       |
'''
sample = """
def on_click(ctx,id,value):
    ctx.elements["output"].value = ctx.elements["carInput"].value

def on_change(ctx,id,value):
    ctx.elements["carInput"].value = value

def datalist_example():
    input(list="cars",placeholder="Choose a car",id="carInput").on("change",on_change)
    with datalist(id="cars"):
        option("Ford")
        option("Volvo")
        option("BMW")
    button("Submit").on("click",on_click)
    text("",id="output")
"""
