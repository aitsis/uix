from ..core.element import Element
print("Imported: col")
class col(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)
        self.classes.append("col")

    def align(self, align):
        self.styles["justify-content"] = align
        return self


title = "Column"

description = '''
## col(value,id = None)
1. Temel column elementi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Column elementinin id'si                         |
| value         | Column elementinin içeriği                      |
'''

sample = """
def column_example():
    with border(""):
        with col(""):
            div("Column 1")
            div("Column 1")
    with border(""):
        with col(""):
            div("Column 2")
            div("Column 2")
"""