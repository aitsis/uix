import os
import tempfile
import shutil
import uix

from ..core.element import Element

uix.html.add_script("file", beforeMain = False, script =
'''
    this.genRandomNumbers = () => {
    const array = new Uint32Array(10);
    crypto.getRandomValues(array);
    return Array.from(array).map(n => n.toString(16)).join('');
    };
    
    async function clientEmit(id, newValue, event_name) {
    if (newValue instanceof File) {
        if (newValue.size > 100 * 1024 * 1024) {
            alert("File size exceeds the limit.");
            return;
        }
        return await uploadFile(newValue, id);
    }
    socket.emit('from_client', { id: id, value: newValue, event_name: event_name });
    }

    async function uploadFile(newValue, id) {
        const uid = genRandomNumbers();
        const formData = new FormData();
        formData.append("file", newValue);
        formData.append("id", id);
        formData.append("uid", uid);

        socket.emit('from_client', { id: id, value: { uid: uid, file_name: newValue.name }, event_name: 'file-change-started' });

        // FOR PYTHON USAGE MAKE CALL TO /file-upload
        //url to call = /file-upload

        return fetch("/api/images/", {
            method: "POST",
            body: formData,
            credentials: "include",
        })
            .then(async (response) => {
                if (!response.ok) {
                    let error = await response.json();
                    throw new Error(error.message ? error.message : response.statusText);
                }
                return response.json();
            })
            .then((data) => {
                socket.emit('from_client', { id: id, value: { uid: uid, file_name: newValue.name, data }, event_name: 'file-upload-started' });
            })
            .catch((error) => {
                if (window.comp_alert) {
                    const inputElement = document.getElementById(id);
                    if (inputElement) {
                        inputElement.value = '';
                    }
                    window.comp_alert.open('alert-danger', error.message);
                    socket.emit('from_client', { id: id, value: { 'error':'error'}, event_name: 'file-upload-error' });
                    return;
                }
                alert(error.message);
            });
    }    
''')
                    

class file(Element):
    def __init__(self,
                 value = None,
                 id = None,
                 multiple = False,
                 save_path = None,
                 on_upload_done = None,
                 on_upload_started = None,
                 on_error = None,
                 accept = None,
                 useAPI=False):
        super().__init__(value = value, id = id)
        self.tag = "input"
        self.value_name = "value"
        self.attrs["type"] = "file"
        self.attrs["name"] = "file"
        self.attrs["multiple"] = multiple
        self.save_path = save_path
        self.events["file-upload-started"] = self.upload_started_API if useAPI else self.upload_started
        self.events["file-change-started"] = self.on_change_started
        self.events["file-upload-error"] = self.on_upload_error
        self.on_upload_started = on_upload_started
        self.on_upload_done = on_upload_done
        self.on_error = on_error
        self.attrs["accept"] = "image/png, image/jpeg" if accept is None else accept

        self.on("change", self.upload_started_API if useAPI else self.upload_started)

    def get_client_handler_str(self, event_name):
        if event_name in ["input","change"]:
            return f" on{event_name}='clientEmit(this.id,this.files[0],\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

    def upload_done(self, uploaded_file_path, uploaded_file_name, data=None):
        try:
            if not self.useAPI:
              if self.save_path:
                  save_file_path = os.path.join(self.save_path, uploaded_file_name)
                  shutil.move(uploaded_file_path, save_file_path)
                  self.on_upload_done(save_file_path)
            else:
                if data:
                    self.on_upload_done(data)
        except Exception as e:
            #print(e)
            pass

    def upload_started(self, id, file):
        uploaded_file_path = os.path.join(tempfile.gettempdir(), file["uid"])
        uploaded_file_name = file["file_name"]

        if os.path.exists(uploaded_file_path):
            # check if the file is used by another process
            try:
                with open(uploaded_file_path, "rb") as f:
                    f.close()
                self.upload_done(uploaded_file_path, uploaded_file_name)
                return
            except Exception as e:
                #print(e)
                pass
        else:
            #print("File not found:", uploaded_file_path)
            return -1

    def upload_started_API(self, id, data):
        try:
            self.upload_done(None, None, data=data)
            return
        except Exception as e:
            pass

    def on_change_started(self, id, value):
        if self.on_upload_started:
            self.on_upload_started(value)
        else:
            pass

    def on_upload_error(self, id, value):
        if self.on_error:
            self.on_error(value)
        else:
            pass

            
            
title = "File"
description = """
# file(value,id = None, multiple = False, save_path = None, on_upload_done = None, on_upload_started = None, on_error = None, accept = None)

1. File elementi. Bir dosya seçme penceresi açar.

    | attr                 | desc                                                               |
    | :------------------- | :----------------------------------------------------------------- |
    | value                | Elementin value'su.                                                |
    | id                   | Elementin içeriği.                                                 |
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
