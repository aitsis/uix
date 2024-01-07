
import uix
from ..core.element import Element

uix.html.add_script("file", script =
"""
const onFileChange = (id,files,eventName) => {
    urls = [];
    for (let i = 0; i < files.length; i++) {
        urls.push(URL.createObjectURL(files[i]));
    }
    clientEmit(id,urls,eventName);
    // const file = files[0];
    // const reader = new FileReader();
    // reader.onload = function(e) {
    //     const data = e.target.result;
    //     const img = document.getElementById(id);
    //     img.src = data;
    //     clientEmit(id,data,eventName);
    // }
    // reader.readAsDataURL(file);
}
""",beforeMain = False)


class file(Element):
    def __init__(self, value=None, id=None, multiple = False):
        super().__init__(value, id)
        self.tag = "input"
        self.attrs["type"] = "file"
        self.attrs["name"] = "file"
        self.attrs["multiple"] = multiple

    def get_client_handler_str(self, event_name):
        if event_name in ["input","change"]:
            return f" on{event_name}='onFileChange(this.id,this.files,\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

title = "File"
description = """
# file(value,id = None, multiple = False, save_path = None, on_upload_done = None, on_upload_started = None, on_error = None, accept = None)

1. File elementi. Bir dosya seçme penceresi açar.

    | attr                 | desc                                                               |
    | :------------------- | :----------------------------------------------------------------- |
    | value                | Elementin içeriği.                                                 |
    | id                   | Elementin id'si                                                    |
    | multiple             | Birden fazla dosya seçilmesine izin verir.                         |
    | save_path            | Dosyanın kaydedileceği yol.                                        |
    | on_upload_done       | Dosya yüklendiğinde çalışacak fonksiyon.                           |
    | on_upload_started    | Dosya yüklenmeye başladığında çalışacak fonksiyon.                 |
    | on_error             | Dosya yüklenirken hata oluştuğunda çalışacak fonksiyon.            |
    | accept               | Seçilebilir  dosya uzantısı tanımlama (audio/* ,video/*, image/*)  |
    | useAPI               | Dosya yükleme işlemini API üzerinden yapar.                        |
"""
sample = """
from uix.elements import file, div, image, col

def file1():
    with col().cls("border"):
        file("",id="myFile", accept=".png, .jpg")
        image("", id="img").style("margin-top","20px").style("width","300px").style("height","300px")
    
def file_example():
    with div("") as main:
        file1()
    return main

"""
