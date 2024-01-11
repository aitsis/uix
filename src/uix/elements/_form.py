from ..core.element import Element
print("Imported: Form")

enctypes = [
    "application/x-www-form-urlencoded",
    "multipart/form-data",
    "text/plain"
]
class form(Element):
    def __init__(
        self,
        value: str=None,
        id: str=None,
        action:str=None,
        method:str=None,
        enctype=enctypes[0],
        ):
        super().__init__(value=value, id=id)
        self.tagname = "form"
        if method is not None:
            self.attrs["method"] = method
        
        if enctype is not None:
            self.attrs["enctype"] = enctype
            
        if action is not None:
            self.attrs["action"] = action
            
            
title = "Form"

description = '''
## form(value,id,action,method,enctype)
1. Temel form elementi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| value         | Formun içeriği                                    |
| id            | Formun id'si                                      |
| action        | Form submit edildiğinde verilerin nereye gönderileceğini belirtir |
| method        | Form verilerini gönderirken kullanılacak HTTP yöntemini belirtir (get,post) |
| enctype       | Form verilerinin sunucuya gönderilirken nasıl kodlanması gerektiğini belirtir (yalnızca method = "post" için) |
'''

sample = """
def comp1():
    with form(id="myForm") as form1:
        form1.cls("border")
        with grid("",columns="1fr 4fr") as grid1:
            grid1.style("gap","10px")
            grid1.style("padding","10px")
            grid1.style("width","300px")
            with col().style("font-size","20px"):
                label("Name", usefor="name")
                label("Email", usefor="email").style("margin-top","10px")
            with col():
                input("", id="name",  placeholder="Enter your name")
                input("", id="email",  placeholder="Enter your email").style("margin-top","10px")
        
            button("Submit").style("margin-top","10px")

 """