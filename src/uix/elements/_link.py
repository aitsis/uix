from ..core.element import Element
print("Imported: link")

class link(Element):
    def __init__(self,value,id = None, href = None, title="", target=""):
        super().__init__(value, id = id)
        self.tag = "a"
        self.value_name ="innerHTML"
        self.attrs["href"] = href
        self.attrs["title"] = title
        self.attrs["target"] = target



title = "Link"

description = '''
Link elementi. Html'deki a elementine karşılık gelir. Sayfaya bağlantı eklemek için kullanılır.

id= Link elementinin id'si
value= Link elementinin yazısı
href= Link elementinin href'i
title= Kullanıcı linkin üzerine geldiğinde göreceği yazı
target= Linkin açılacağı pencere seçeneği
'''

sample = """
with parent(''):
    link("Google", href="https://www.google.com.tr", target="_blank", title="Google'a git")
"""