from ..core.element import Element
print("Imported: Button")
class button(Element):
    def __init__(self,value:str,id:str = None, type:str='button', formID:str=None, disabled:bool=False):
        super().__init__(value, id = id)
        self.tag = "button"
        self.attrs["type"] = type
        self.value_name = "innerHTML"
        self.disabled = disabled

        if formID is not None:
            self.attrs["form"] = formID

        if self.disabled:
            self.attrs["disabled"] = "disabled"

    def bind(self,session):
        if self.id is None:
            self.id = "btn_" + str(session.next_id())
        super().bind(session)
        

title = "Button"

description = '''
## button(value,id = None, type='button', formID=None, disabled=False)
1. Temel buton elementi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Buton elementinin id'si                          |
| value         | Buton elementinin içeriği                       |
| type          | Buton elementinin tipi                          |
| formID        | Buton elementinin ait olduğu formun id'si       |
| disabled      | Buton elementinin etkinliğini kapatır           |
'''

sample = """
button_demo_svg = '<g>INFO_SVG_ICERIGI</g>'

def degistir(ctx, id, value):
    ctx.elements["btn-icon1"].value = "fa-solid fa-user"

def button_example():
    with div().cls("row").style("gap","10px") as main:
        button("Değiştir").on("click", degistir)
        button("Sarı").cls("btn-warning")
        button("Kırmızı").cls("btn-red")
        button("Info").cls("btn-info")
        button("Reset", type="reset").cls("btn-reset")
        with button("", id="myID", type="sumbit").cls("btn-svg-demo"):
            svg(button_demo_svg).size(20,20).viewbox("0,0,512,512")
        with button("", id="btn-fontawesome").cls("btn-inactive btn-svg-demo").style("color","black"):
            icon(id= "btn-icon1", value= "fa-solid fa-house")
        button("Disabled", disabled=True)
            
    return main
"""
