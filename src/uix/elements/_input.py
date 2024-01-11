from ..core.element import Element
print("Imported: input")
class input(Element):
    def __init__(self,value:str = None,id:str = None,type: str='text',name:str=None,placeholder:str="",required:bool=False,list:str=None):
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
        
        if list is not None:
            self.attrs["list"] = list
        
        if step is not None:
            self.attrs["step"] = step

        if min is not None:
            self.attrs["min"] = min
        
        if max is not None:
            self.attrs["max"] = max

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self
    

title = "Input"

description = '''
## input(value,id,type,name,placeholder,step,required)
1. Temel input elementi.
<<<<<<< HEAD
    | attr          | desc                                            |
    | :------------ | :-----------------------------------------------|
    | id            | Input elementinin id'si                         |
    | value         | Input elementinin içeriği                       |
    | type          | Input elementinin tipi                          |
    | name          | Input elementinin name'i                        |
    | placeholder   | Input elementinin placeholder'i                 |
    | required      | Input elementinin required'u                    |
    | list          | Input elementinin list'i                        |
    | step          | Input elementinin step'i                        |
    | min           | Input elementinin min'i                         |
    | max           | Input elementinin max'i                         |
=======

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Input elementinin id'si                          |
| value         | Input elementinin içeriği                       |
| type          | Input elementinin tipi                          |
| name          | Input elementinin name'i                        |
| placeholder   | Input elementinin placeholder'i                 |
| step          | Input elementinin step'i                        |
| required      | Input elementinin required'u                    |
| list          | Input elementinin list'i                        |
>>>>>>> eac99a1f2d08f3bb067309c66d16ac24de1aabdf
'''
sample = """
def input_example():
    with col("").style("width","min-content").style("gap","10px"):
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
        with row(""):
            div("Zorunlu alanlar doldurulmalıdır.").style("font-size","10px")
            button("Gönder", id="submitButton", type="submit", disabled = True)
"""