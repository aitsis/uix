from ..core.element import Element
print("Imported: col")
class col(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)
        self.classes.append("col")



title = "column"

description = '''
# col(value,id = None)
1. Temel column elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Column elementinin id'si                         |
    | value         | Column elementinin içeriği                      |
'''

sample = """
with parent:
    with border("").style("padding","10px"):
        with col(""):
            div("Column 1")
            div("Column 1")
    with border("").style("padding","10px"):    
        with col(""):
            div("Column 2")
            div("Column 2")
"""