from ..core.element import Element
from ._border import border as border

class border(Element):
    """
    # border(value,id)
    1. Border elementi. Kenarında 1px kalınlığında çizgi bulunan bir div oluşturur.

    İçerisine elemanlar eklenerek kullanılır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Border elementinin id'si                          |
    | value         | Border elementinin içeriği                       |
    """
    def __init__(self, value = None, id = None) -> None: ...
    
        