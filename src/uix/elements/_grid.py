from ..core.element import Element
print("Imported: grid")
class grid(Element):
    def __init__(self,value,id = None, columns = None, rows = None):
        super().__init__(value, id = id)
        self.style("display", "grid")
        if columns is not None:
            self.style("grid-template-columns", columns)
        else:
            self.style("grid-template-columns", "auto auto")
        if rows is not None:
            self.style("grid-template-rows", rows)
        else:
            self.style("grid-template-rows", "auto auto")

    

title = "Grid"

description = '''
# grid(value,id,columns,rows)
1. Grid elementi. Grid özelliğinde bir div oluşturur. column ve row değerleri girilerek içerisindeki elemanlar grid özelliğine göre konumlandırılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Grid elementinin id'si                          |
    | value         | Grid elementinin içeriği                       |
    | columns       | Grid elementinin sütun değerlerini belirler. Örneğin: "150px 600px" |
    | rows          | Grid elementinin satır değerlerini belirler. Örneğin: "150px 600px" |
'''


sample = """
with grid("",columns = "150px 600px 200px",rows="auto auto"):
    with div(""):
        text("Column1, Row1")
    with div(""):
        text("Column2, Row1")
    with div(""):
        text("Column3, Row1")
    with div(""):
        text("Column1, Row2")
    with div(""):
        text("Column2, Row2")
    with div(""):
        text("Column3, Row2")   ## 3 sütun 2 satırlık bir grid alanı oluşturduk.
"""

