from ..core.element import Element
print("Imported: source")

class source(Element):
    def __init__(self,value,id = None, media = None,type ="video/mp4"):
        super().__init__(value, id = id)
        self.tag = "source"
        self.value_name = "src"
        self.has_content = False
        self.attrs["media"] = media
        self.attrs["type"] = type



title = "Source"

description = '''
Html'deki source elementine karşılık gelir. Medya öğelerinde birden fazla kaynak belirtmek için kullanılır. Bunun sebebi tarayıcıların farklı formatları desteklemesidir.
id= Source elementinin id'si
value= Source elementinin src'si
media= CSS'de normalde tanımlanacak herhangi bir geçerli medya sorgusunu kabul eder.
type= Kaynak dosyanın MIME türü. Örneğin, video/mp4, video/webm veya video/ogg. 
Type'ı farklı birden fazla source belirtilirse tarayıcı desteklediği ilk kaynağı kullanır.
Default değeri video/mp4'dür.
'''

sample = """
with video():
    source(value="video.mp4")
    source(value="video.webm",type="video/webm")
    source(value="video.ogg",type="video/ogg")
"""
