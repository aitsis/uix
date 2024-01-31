
import uix
from ..core.element import Element
from ..core.file import File
uix.html.add_script("file", script =
"""
const onFileChange = (id,files,eventName) => {
    urls = [];
    for (let i = 0; i < files.length; i++) {
        urls.push({ name:files[i].name,
                    size:files[i].size,
                    type:files[i].type,
                    lastModified:files[i].lastModified,
                    lastModifiedDate:files[i].lastModifiedDate,
                    url:URL.createObjectURL(files[i])
                });
    }
    clientEmit(id,urls,eventName);
};
event_handlers["file-upload"] = (id,url,eventName) => {
    console.log("file-upload",id,url,eventName);
    fetch(url).then(response => response.blob()).then(data => 
    {
        console.log(data);
        const xhr = new XMLHttpRequest();
        xhr.upload.onprogress = function(event) {
            if (event.lengthComputable) {
                const percentComplete = 100 * event.loaded / event.total;
                clientEmit(id,{"status":"progress","url":url,"progress":percentComplete},eventName);
            }
        };
        xhr.onload = function() {
            if (xhr.status === 200) {
                clientEmit(id,{"status":"progress","url":url,"progress":100},eventName);
                clientEmit(id,{"status":"done","url":url},eventName);
            } else {
                clientEmit(id,{"status":"error","url":url, "error": xhr.responseText }, eventName);
            }
        };
        xhr.onerror = function() {
            clientEmit(id,{"status":"error","url":url, "error": xhr.responseText }, eventName);
        };
        xhr.open("POST", "/upload/"+url);
        xhr.send(data);
        console.log("uploading");
    });
};
""",beforeMain = False)


class file(Element):
    """
    File elementi. Bir dosya seçme penceresi açar.
    callback(ctx, event, data, status)
    """
    def __init__(self, value: str=None, id:str =None, multiple:bool = False, callback = None, accept:bool = False):
        super().__init__(value, id)
        self.tag = "input"
        self.attrs["type"] = "file"
        self.attrs["name"] = "file"
        self.attrs["multiple"] = multiple
        self.attrs["accept"] = accept
        self.callback = callback
        self.events["change"] = self.on_change
        self.events["file-upload"] = self.on_file_upload
    def get_client_handler_str(self, event_name):
        if event_name in ["input","change"]:
            return f" on{event_name}='onFileChange(this.id,this.files,\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

    def upload(self, url):
        self.session.send(self.id, url , "file-upload")

    def on_change(self, ctx, id ,value):
        if self.callback is None:
            return
        if isinstance(value, list):
            files = []
            for file in value:
                files.append(File(**file))
            self.callback(ctx, id, "select", files, "done")
        else:
            self.callback(ctx, id, "select", "No selected files", "error")
                
    def on_file_upload(self, ctx, id, value):
        if self.callback is None:
            return
        url = value["url"]
        status = value["status"]
        if status == "error":
            error_message = value["error"]
            self.callback(ctx, id, "upload", error_message, status)
            return
        if status == "progress":
            progress = value["progress"]
            self.callback(ctx, id, "upload", {"url": url, "progress":progress}, "progress")
            return
        data = uix.files[url]["data"]
        uix.files[url]["data"] = None
        if data is None:
            self.callback(ctx, id, "upload", "Internal Server Error. File not uploaded", "error")
            return
        self.callback(ctx, id, "upload", data, "done")

title = "File"
description = """
## file(value,id = None, multiple = False, save_path = None, on_upload_done = None, on_upload_started = None, on_error = None, accept = None)

1. File elementi. Bir dosya seçme penceresi açar.

| attr                 | desc                                                               |
| :------------------- | :----------------------------------------------------------------- |
| value                | Elementin içeriği.                                                 |
| id                   | Elementin id'si                                                    |
| multiple             | Birden fazla dosya seçilmesine izin verir.                          |
| accept               | Seçilebilecek dosya tiplerini belirtir.                             |
| callback             | Dosya seçildiğinde çağrılacak fonksiyon.                            |
"""
sample = """
import uix
from uix.elements import file, div, image, col, row, progress, check, button, container
from uix.elements._file import title, description, sample as code

from uix.core.file import File 
def lineitem(value):
    div(value).style("padding","5px;")
    
def upload_file(ctx, id, value):
    print("upload_file",id)
    ctx.elements["file_123"].upload(id)
    

def line(file):
    with row(id=file.url).style("margin-top","10px").on("click", upload_file) as r:
        image(value=file.url).size(None,100)
        lineitem(file.name)
        lineitem(file.size)
        lineitem(file.type)
        progress(id = file.url+"_progress")
            

def list_files(ctx, files):
    with ctx.elements["files"]:
        for file in files:
            line(file)
    ctx.elements["files"].update()

def show_error(ctx, error):
    with ctx.elements["files"]:
        div(error).style("color","red")
    ctx.elements["files"].update()


def select_callback(ctx, id, data, status):
    if status == "done":
        list_files(ctx, data)
    else:
        show_error(ctx, data)

def upload_callback(ctx, id, data, status):
    if status == "done":
        print("upload done",len(data))
        #>>>>>>>>>>>>>>>>>>>
        # USE DATA HERE
        #<<<<<<<<<<<<<<<<<<<<
    elif status == "progress":
        ctx.elements[data["url"] + "_progress"].value = data["progress"]
    else:
        show_error(ctx, data)

def file_callback(ctx, id, event, data, status):
    if event == "select":
        select_callback(ctx, id, data, status)    
    elif event == "upload":
        upload_callback(ctx, id, data, status)


def file_example():
    multiple = False
    with container() as root:
        with row(id="root").center():
            check(multiple, id="multiple", disabled = False).on("change", lambda ctx, id, value: ctx.elements["file_123"].set_attr("multiple",value))
            file(id="file_123", multiple=multiple,callback = file_callback, accept="image/png,image/jpeg,image/gif")
        div("Files:", id="files").style("margin-top","10px")
    return root

"""
