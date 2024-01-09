from ..core.element import Element
from ._border import border as border
from ._button import button as button

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
    
class button(Element):
    """
    # button(value,id = None, callback = None, color = None, size = None, icon = None)
    1. Buton elementi. Butonun içeriğini belirler.

        | attr          | desc                                              |
        | :------------ | :------------------------------------------------ |
        | id            | Buton elementinin id'si                          |
        | value         | Buton elementinin içeriği                       |
        | callback      | Buton elementine tıklandığında çalışacak fonksiyon |
        | color         | Buton elementinin rengi                         |
        | size          | Buton elementinin boyutu                        |
        | icon          | Buton elementinin içerisindeki ikon             |
    """
    def __init__(self, value = None, id = None, callback = None, color = None, size = None, icon = None) -> None: ...