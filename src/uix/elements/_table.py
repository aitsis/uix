from ..core.element import Element

class table(Element):
    def __init__(self,value:str,id:str = None):
        super().__init__(value, id = id)    
        self.tag = "table"

title = "Table"
description = '''
## table(value,id = None)
1. Table elementi. Html'deki table elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Table elementinin id'si                          |
| value         | Table elementinin içeriği                       |
'''
sample = """
import uix
from uix.elements import table, tr, td, tbody, th, thead, row # type: ignore
from uix.elements._table import title, description, sample as code

uix.html.add_css("custom-table",'''
          
#custom-table thead {    
  background-color: #ff000026;
} 

#custom-table tr:nth-child(even){ 
  background-color: black;
}
                 
}
''')


fake_data = [DATA JSON BURAYA]

def table_example():
    global fake_data
    with row().style("width: max-content; gap: 10px;"):
        with table("", id="table_example"):
            with thead("",id="table_example_header"):
                with tr("",id="table_example_header_row"):
                    th("ID")
                    th("Name")
                    th("Username")
                    th("Email")
            with tbody("",id="table_example_body"):
                for item in fake_data:
                    with tr("",id=item["id"]):
                        td(item["id"])
                        td(item["name"])
                        td(item["username"])
                        td(item["email"])

        with table("", id="custom-table"):
            with thead(""):
                with tr(""):
                    th("ID")
                    th("Name")
                    th("Username")
                    th("Email")
            with tbody("",id="custom-table_body"):
                for item in fake_data:
                    with tr("",id="custom-"+str(item["id"])):
                        td(item["id"])
                        td(item["name"])
                        td(item["username"])
                        td(item["email"])
"""
