from ..core.element import Element
print("Imported: details")

class details(Element):
    def __init__(self,value:str = None, id:str = None):
        super().__init__(value=value, id = id)
        self.tag = "details"
        

title = "Details"

description = '''
## details(value,id = None)

1. Details elementi. Bilgilerin yalnızca widget "açık" duruma getirildiğinde görülebildiği bir açıklama widget'ı oluşturur.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Details elementinin id'si                          |
| value         | Details elementinin başlığı                       |

'''

sample = """

with div("",) as details_example:
    with details("Details Example"):
        text("Details Content")

"""