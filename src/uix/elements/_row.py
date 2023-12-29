from ..core.element import Element
print("Imported: row")
class row(Element):
    def __init__(self,value,id = None):
        super().__init__(value, id = id)
        self.classes.append("row")



title = "Row"
description = '''
Row elementi. Temel olarak bir satırı temsil eder. İçerisindeki elemanları yan yana ekler.
'''
sample = """
with row():
    button("Buton",id="btn1")
    button("Buton",id="btn2")
    button("Buton",id="btn3")
"""

