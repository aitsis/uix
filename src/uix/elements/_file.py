
import uix
from ..core.element import Element
from ..core.file import File

file_script = """
const onFileChange = (id,files,eventName) => {
    urls = [];
    for (let i = 0; i < files.length; i++) {
        urls.push({ name:files[i].name,
                    size:files[i].size,
                    type:files[i].type,
                    lastModified:files[i].lastModified,
                    url:URL.createObjectURL(files[i])
                });
    }
    clientEmit(id,urls,eventName);
};
event_handlers["file-upload"] = (id,url,eventName) => {
    fetch(url).then(response => response.blob()).then(data =>
    {
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
    });
};
"""

class file(Element):
    """
    File elementi. Bir dosya seçme penceresi açar.
    callback(ctx, event, data, status)
    """
    def __init__(self, value: str=None, id:str =None, multiple:bool = False, callback = None, accept:bool = False):
        super().__init__(value, id)
        self.register_script("file_script", file_script)
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
