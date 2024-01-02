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
        value=None,
        id=None,
        action=None,
        method=None,
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
# form(value,id,action,method,enctype)
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
    with parent:
        form("Form",id="form1", action="http://localhost:8080", method="post", enctype="multipart/form-data")

 """