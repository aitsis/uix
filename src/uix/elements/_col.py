from ..core.element import Element
print("Imported: col")
class col(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)
        self.classes.append("col")



title = "column"
description = '''
Temel column elementi.
value : column içeriği
id : column id'si
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