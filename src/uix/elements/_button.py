from ..core.element import Element
print("Imported: Button")
class button(Element):
    def __init__(self,value:str,id:str = None, type:str='button', formID:str=None, disabled:bool=False):
        super().__init__(value, id = id)
        self.tag = "button"
        self.attrs["type"] = type
        self.value_name = "innerHTML"
        self.classes.append("btn")
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
# button(value,id = None, type='button', formID=None, disabled=False)
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
def button_example():
    main = button("Click me!")
    return main
"""
