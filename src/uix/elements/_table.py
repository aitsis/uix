from ..core.element import Element

class table(Element):
    def __init__(self,id = None,value = None):
        super().__init__(value, id = id)    
        self.tag = "table"

title = "Table"
description = """
Temel html tablo etiketidir.
value: tablo değeri
id: tablo id değeri
"""
sample = """
with table():
    with tr():
        with th():
            text("Başlık 1")
        with th():
            text("Başlık 2")
        with th():
            text("Başlık 3")
    with tr():
        with td():
            text("Değer 1")
        with td():
            text("Değer 2")
        with td():
            text("Değer 3")
"""
