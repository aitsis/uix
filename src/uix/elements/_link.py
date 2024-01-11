from ..core.element import Element

print("Imported: link")

class link(Element):
    def __init__(self,value:str,id:str = None, href:str = None, title:str="", target:str=""):
        super().__init__(value, id = id)
        self.tag = "a"
        self.value_name ="innerHTML"
        self.attrs["href"] = href
        self.attrs["title"] = title
        self.attrs["target"] = target

title = "Link"

description = '''
# link(value,id,href,title,target)
1. Link elementi. Html'deki a elementine karşılık gelir. Sayfaya bağlantı eklemek için kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Link elementinin id'si                            |
| value         | Link elementinin yazısı                           |
| href          | Link elementinin href'i                           |
| title         | Kullanıcı linkin üzerine geldiğinde göreceği yazı |
| target        | Linkin açılacağı pencere seçeneği                 |
'''

sample = """
with parent(''):
    link("Ai Ait",href="https://ai.ait.com.tr/",target="_blank",title="Ai Ait Website'sine Git") 
    
"""