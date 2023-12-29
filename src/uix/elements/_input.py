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
    

    title = "input"
    description = '''
    Temel input elementi.
    value : Inputun otomaik olarak doldurulacak değeri
    id : Inputun id'si
    type : Inputun type değerleri (text, password, email, date, datetime, time, tel)
    name : Input alanının form gönderildiğinde sunucuya gönderilecek verinin adını belirtir.
    placeholder : Inputun açıklama metni
    step : Inputun sayısal değerlerde artış miktarı
    required : Inputun zorunlu olup olmadığı
    '''
    sample = """
    with parent:
        input("", placeholder="Kullanıcı Adı")
        input("",type="password", placeholder="Şifre")
        input("",type="number", placeholder="Sayı")
        input("2024-01-01T00:00",type="datetime-local", placeholder="Tarih ve Saat")
        input("",type="date")
        input("",type="time")
    """