from ..core.element import Element

class table(Element):
    def __init__(self,value:str,id:str = None):
        super().__init__(value, id = id)    
        self.tag = "table"

title = "Table"
description = '''
# table(value,id = None)
1. Table elementi. Html'deki table elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Table elementinin id'si                          |
| value         | Table elementinin içeriği                       |
'''
sample = """
def table_example():
    with table("", id="table_example"):
        global fake_data
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
"""
