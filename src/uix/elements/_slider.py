from ..core.element import Element
print("Imported: slider")

class slider(Element):
    def __init__(self, value=None, id=None, min=0, max=100, step=1,):
        super().__init__(value=value, id=id)
        self.min = min
        self.max = max
        self.step = step
        self.tag = "input"
        self.value_name = "value"
        self.has_content = False
        self.attrs["type"] = "range"
        self.attrs["min"] = self.min
        self.attrs["max"] = self.max
        self.attrs["step"] = self.step
        
    def disable(self):
        self.attributes["disabled"] = "disabled"
        return self
    
title = "Slider"
description = """
# slider(value,id,min,max,step)
1. Slider bir input elementidir.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Slider elementinin id'si                          |
    | value         | Slider elementinin içeriği                       |
    | min           | Slider elementinin minimum değeri                |
    | max           | Slider elementinin maksimum değeri               |
    | step          | Slider elementinin artış değeri                  |
"""
sample = """

    def on_slider_change():
        print("Slider değeri değişti")
        print("Yeni değer: ",slider1.value)
    with parent:
        slider(id="slider1",min=0,max=100,step=1).on("change",lambda: on_slider_change())
        
"""