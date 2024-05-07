from ..core.element import Element
print("Imported: summary")
class summary(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)
        self.tag = "summary"


title = "Summary"

description = '''
## summary(value,id = None)
1. Summary elementi. Details elementinin açıklama başlığı olarak kullanılan bir elementtir.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Summary elementinin id'si                        |
| value         | Summary elementinin içeriği                      |
'''

sample = """
def summary_example():
    with details() as summary_example:
        summary(value="Details main title")
        label(value="Details Content")
    return summary_example
"""