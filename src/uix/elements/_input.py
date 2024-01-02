from ..core.element import Element
print("Imported: input")
class input(Element):
    def __init__(self,value = None,id = None,type='text',name=None,placeholder="",required=False):
        super().__init__(value, id = id)
        self.tag = "input"
        self.value_name = "value"
        self.has_content = False

        if type is not None:
            self.attrs["type"] = type
        
        if placeholder is not None:
            self.attrs["placeholder"] = placeholder

        if name is not None:
            self.attrs["name"] = name

        if required:
            self.attrs["required"] = "required"

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self
    

title = "Input"

description = '''
# input(value,id,type,name,placeholder,step,required)
1. Temel input elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Input elementinin id'si                          |
    | value         | Input elementinin içeriği                       |
    | type          | Input elementinin tipi                          |
    | name          | Input elementinin name'i                        |
    | placeholder   | Input elementinin placeholder'i                 |
    | step          | Input elementinin step'i                        |
    | required      | Input elementinin required'u                    |
'''
sample = """
def input_example():
    with col("").style("height","min-content").style("width","min-content").style("gap","10px"):
        input("", placeholder="Kullanıcı Adı", required=True)
        input("",type="password", placeholder="Şifre")
        input("",type="number", placeholder="Sayı")
        input("2024-01-01T00:00",type="datetime-local", placeholder="Tarih ve Saat")
        input("",type="date")
        input("",type="time")    
    
    def on_change(ctx, id, value):
        if value!= "":
            ctx.elements["submitButton"].attrs.pop("disabled", None)
            ctx.elements["submitButton"].update()
            
        else:
            ctx.elements["submitButton"].attrs["disabled"] = True
            ctx.elements["submitButton"].update()
                    
    with border("").style("padding","20px").style("width","50%"):
        input(id="userName", placeholder="Kullanıcı Adı", required=True).on("input",on_change)
        with row("").style("display","flex").style("justify-content","space-between"):
            div("Zorunlu alanlar doldurulmalıdır.").style("font-size","10px")
            button("Gönder", id="submitButton", type="submit", disabled = True)
"""