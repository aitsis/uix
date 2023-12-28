from ..core.element import Element
print("Imported: Check")
class check(Element):
    def __init__(self, value = None, checked = False, id = None, disabled = False ):
        super().__init__(value, id = id)
        self.tag = "input"
        self.attrs["type"] = "checkbox"
        self.value_name = "checked"
        self.classes.append("form-check-input")
        self.disabled = disabled

        if self.disabled:
            self.attrs["disabled"] = "disabled"
    def checked(self):
        self.attrs["checked"] = "checked"
        return self

title = "Check"
description = """
Checkbox bir input elementidir.
checked : Check'in seçili olup olmadığı
id : Check'in id'si
disabled : Check'in etkinliğini kapatır.
events : Check'e ait eventler:
    click : Check'e tıklandığında
with parent:
    check("Check 1",id="check1").on("click",lambda: print("Tıklandı"))

"""
sample = """
with parent:
    check("Check 1",id="check1")
    check("Check 2",id="check2")
    check("Check 3",id="check3")
    check("Check 4",id="check4")
"""