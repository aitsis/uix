from ..core.element import Element
print("Imported: icon")
class icon(Element):
    def __init__(self,value:str = None,id:str = None):
        super().__init__(value, id = id)
        self.tag="i"
        self.value_name=None
        self.classes.append(value)

    # DIŞARDAN VALUE İLE CLASS DEĞİŞTİREBİLMEK İÇİN ---------------------------------------------------------------
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        for cls in self.value.split(" "):
            self.remove_class(cls)
        self._value = value
        for cls in value.split(" "):
            self.add_class(cls)
    # DIŞARDAN VALUE İLE CLASS DEĞİŞTİREBİLMEK İÇİN ---------------------------------------------------------------


title = "Icon"

description = '''
## icon(value,id = None)
1. Icon elementi. Html'deki i elementine karşılık gelir. Fontawesome sınıfları kullanılarak svg iconlar oluşturulabilir.
2. https://fontawesome.com/search?o=r&m=free adresinden kullanılabilir iconlara ulaşılabilir.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Icon elementinin id'si                            |
| value         | Fontawesome sitesinden alınan classlar kullanılır |
'''

sample = """
from uix.elements import icon # type: ignore

def icon_example():
    main = icon("fa-solid fa-house fa-10x")
    return main
"""
        