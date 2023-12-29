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
description = '''
Slider elementi. Değer değiştiğinde bir fonksiyon çağırılabilir.
value : Sliderın değeri
id : Sliderın id'si
min : Sliderın minimum değeri
max : Sliderın maksimum değeri
step : Sliderın artış miktarı
events : Slidera ait eventler:
    change : Sliderın değeri değiştiğinde
'''
sample = """

    def on_slider_change():
        print("Slider değeri değişti")
        print("Yeni değer: ",slider1.value)
    with parent:
        slider(id="slider1",min=0,max=100,step=1).on("change",lambda: on_slider_change())
        
"""