from ..core.element import Element
print("Imported: border")
class border(Element):
    def __init__(self,value,id = None):
        super().__init__(value, id = id)
        self.classes.append("border")

title = "Border"

description = '''
# border(value,id)
1. Border elementi. Kenarında 1px kalınlığında çizgi bulunan bir div oluşturur.
İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Border elementinin id'si                          |
    | value         | Border elementinin içeriği                       |
'''

sample = """
def button_generator(value):
    button(value)


for i in range(len(example_button)):
    with border("",) as border_demo:
        button_generator(example_button[i])

"""