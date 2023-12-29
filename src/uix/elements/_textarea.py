from ..core.element import Element

class textarea(Element):
    def __init__(self, id = None, value = None ,placeholder = None):
        super().__init__(value, id = id)
        self.tag = "textarea"
        self.attrs["placeholder"] = placeholder
        self.classes.append("textarea")

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self
    

title = "Textarea"
description = """
Temel metin giriş alanıdır.
value: Varsayılan değer
id: id değeri
placeholder: placeholder değeri
"""
sample = """
textarea(placeholder = "Bir şeyler yazın..."):
"""