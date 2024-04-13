from ..core.element import Element
print("Imported: grid")
class grid(Element):
    def __init__(self,value:str = None, id:str = None, columns:str = None, rows:str = None):
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
## grid(value,id,columns,rows)
1. Grid elementi. Grid özelliğinde bir div oluşturur. column ve row değerleri girilerek içerisindeki elemanlar grid özelliğine göre konumlandırılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Grid elementinin id'si                          |
| value         | Grid elementinin içeriği                       |
| columns       | Grid elementinin sütun değerlerini belirler. Örneğin: "150px 600px" |
| rows          | Grid elementinin satır değerlerini belirler. Örneğin: "150px 600px" |
'''


sample = """
 with grid("",columns= "40% 1fr").style("margin","auto") as grid1:
        grid1.style("width","400px")
        grid1.style("border","1px #aaa solid")
        grid1.style("padding","10px")
        grid1.style("gap","10px")
        grid1.style("border-radius","10px")
        button1("A!")
        button1("B!")
        button1("C!")
        button1("D!")
"""

