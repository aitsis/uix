from ..core.element import Element
from uix.elements._canvas import _canvas
class canvas(Element):
    '''
# canvas(value,id = None)
1. Canvas elementi. Html'deki canvas elementine karşılık gelir. Genellikle Komponentler içinde kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Canvas elementinin id'si                          |
    | width         | Canvas elementinin genişliği (piksel olarak)      |
    | height        | Canvas elementinin yüksekliği (piksel olarak)     |
'''
    def __init__(self,id = None, width = 300, height = 150)-> None: ...
from uix.elements._border import _border
class border(Element):
    '''
# border(value,id)
1. Border elementi. Kenarında 1px kalınlığında çizgi bulunan bir div oluşturur.
İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Border elementinin id'si                          |
    | value         | Border elementinin içeriği                       |
'''
    def __init__(self, value = None, id = None)-> None: ...
from uix.elements._row import _row
class row(Element):
    '''
# row(value,id)
1. Row elementi. Temel olarak bir satırı temsil eder. İçerisindeki elemanları yan yana ekler.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Row elementinin id'si                          |
    | value         | Row elementinin içeriği                       |
'''
    def __init__(self,value = None,id = None)-> None: ...
from uix.elements._source import _source
class source(Element):
    '''
# source(value,id,media,type)
1. Source elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Source elementinin id'si                          |
    | value         | Source elementinin src'si                       |
    | media         | CSS'de normalde tanımlanacak herhangi bir geçerli medya sorgusunu kabul eder. |
    | type          | Kaynak dosyanın MIME türü. Örneğin, video/mp4, video/webm veya video/ogg. |
'''
    def __init__(self,value,id = None, media = None,type ="video/mp4")-> None: ...
from uix.elements._tbody import _tbody
class tbody(Element):
    '''
# tbody(value,id = None)
1. Tbody elementi. Html'deki tbody elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Tbody elementinin id'si                          |
    | value         | Tbody elementinin içeriği                       |
'''
    def __init__(self,value = None, id = None,name = None)-> None: ...
from uix.elements._th import _th
class th(Element):
    '''
# th(value,id = None)

1. Html'deki th elementine karşılık gelir. Tablo başlıkları için kullanılır.
    
        | attr          | desc                                              |
        | :------------ | :------------------------------------------------ |
        | id            | Th elementinin id'si                          |
        | value         | Th elementinin içeriği                       |
    '''
    def __init__(self,value = None, id = None, name = None)-> None: ...
from uix.elements._textarea import _textarea
class textarea(Element):
    """
# textarea(value,id,placeholder)
1. Temel textarea elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Textarea elementinin id'si                          |
    | value         | Textarea elementinin içeriği                       |
    | placeholder   | Textarea elementinin placeholder değeri            |
"""
    def __init__(self, value = None , id = None, placeholder = None)-> None: ...
from uix.elements._listitem import _listitem
class listitem(Element):
    '''
# listitem(value,id)
1. Liste elemanı elementi. Sıralı liste elementine veya sırasız liste elementine eleman eklemek için kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Liste elemanının id'si                          |
    | value         | Liste elemanının içeriği                       |
    | attributes    | Liste elemanına ait attribute'lar              |
    | attrs["class"]| Liste elemanına ait class'lar. Varsayılan değer: list-item |


'''
    def __init__(self,value=None, id=None )-> None: ...
from uix.elements._main import _main
class main(Element):
    '''
# main(value,id = None)

1. Main elementi. Html main elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.

'''
    def __init__(self,value = None, id = None)-> None: ...
from uix.elements._select import _select
class select(Element):
    '''
# select(value,id)
1. Temel select elementi. Tek başına kullanılmaz. Option elementleri ile kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Select elementinin id'si                          |
    | value         | Select elementinin içeriği                       |
    | selected      | Option değerlerinden hangisinin başlangıç değeri olucak tanımlar. |
    | disabled      | Selectin etkinliğini kapatır. |
'''
    def __init__(self,value = None,id = None, disabled=False)-> None: ...
from uix.elements._check import _check
class check(Element):
    """

# check(value,id,checked,disabled)
1. Checkbox bir input elementidir.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Check elementinin id'si                           |
    | value         | Check elementinin içeriği                        |
    | checked       | Check'in seçili olup olmadığı                     |
    | disabled      | Check'in etkinliğini kapatır.                     |
"""
    def __init__(self, value = None, checked = False, id = None, disabled = False )-> None: ...
from uix.elements._text import _text
class text(Element):
    '''
# text(value,id = None)
1. Html'deki p elementine karşılık gelir. Sayfada görüntülenmesi istenen yazılar için kullanılır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Text elementinin id'si                          |
    | value         | Text elementinin içeriği                       |
'''
    def __init__(self,value,id = None)-> None: ...
from uix.elements._tfoot import _tfoot
class tfoot(Element):
    '''
# tfoot(value,id = None)
1. Tablonun alt kısmı için kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | tfoot elementinin id'si                          |
    | value         | tfoot elementinin içeriği                       |
'''
    def __init__(self,value = None, id = None,name = None)-> None: ...
from uix.elements._footer import _footer
class footer(Element):
    '''
# footer(value,id = None)
1. Footer elementi. Html footer elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır. Sayfanın en altında yer alır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Footer elementinin id'si                          |
    | value         | Footer elementinin içeriği                       |
'''
    def __init__(self,value = None, id = None)-> None: ...
from uix.elements._col import _col
class col(Element):
    '''
# col(value,id = None)
1. Temel column elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Column elementinin id'si                         |
    | value         | Column elementinin içeriği                      |
'''
    def __init__(self,value = None,id = None)-> None: ...
from uix.elements._button import _button
class button(Element):
    '''
# button(value,id = None, type='button', formID=None, disabled=False)
1. Temel buton elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Buton elementinin id'si                          |
    | value         | Buton elementinin içeriği                       |
    | type          | Buton elementinin tipi                          |
    | formID        | Buton elementinin ait olduğu formun id'si       |
    | disabled      | Buton elementinin etkinliğini kapatır           |
'''
    def __init__(self,value,id = None, type='button', formID=None, disabled=False)-> None: ...
from uix.elements._form import _form
class form(Element):
    '''
# form(value,id,action,method,enctype)
1. Temel form elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | value         | Formun içeriği                                    |
    | id            | Formun id'si                                      |
    | action        | Form submit edildiğinde verilerin nereye gönderileceğini belirtir |
    | method        | Form verilerini gönderirken kullanılacak HTTP yöntemini belirtir (get,post) |
    | enctype       | Form verilerinin sunucuya gönderilirken nasıl kodlanması gerektiğini belirtir (yalnızca method = "post" için) |
'''
    def __init__(
        self,
        value=None,
        id=None,
        action=None,
        method=None,
        enctype=enctypes[0],
        )-> None: ...
from uix.elements._md import _md
class md(Element):
    '''
# md(value,id)
1. Markdown elementi. Markdown dilinde yazılmış metni html'e çevirir.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Markdown elementinin id'si                          |
    | value         | Markdown elementinin içeriği                       |
'''
    def __init__(self,value = None,id = None)-> None: ...
from uix.elements._file import _file
class file(Element):
    """
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
    def __init__(self, value=None, id=None, multiple = False, callback = None, accept = False)-> None: ...
from uix.elements._unorderedlist import _unorderedlist
class unorderedlist(Element):
    '''
# unorderedlist(value,id,role)
1. Temel unorderedlist elementi listitem elementleri ile kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | unorderedlistin id'si                          |
    | value         | unorderedlistin içeriği                       |
    | role          | unorderedlistin rolü |
'''
    def __init__(self,value = None, id = None, role = None)-> None: ...
from uix.elements._slider import _slider
class slider(Element):
    """
# slider(value,id,min,max,step)
1. Slider bir input elementidir.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Slider elementinin id'si                          |
    | value         | Slider elementinin içeriği                       |
    | min           | Slider elementinin minimum değeri                |
    | max           | Slider elementinin maksimum değeri               |
    | step          | Slider elementinin artış değeri                  |
"""
    def __init__(self, value=None, id=None, min=0, max=100, step=1,)-> None: ...
from uix.elements._image import _image
class image(Element):
    '''
# image(value,id = None)
1. Html'deki img elementine karşılık gelir. Sayfada görüntülenmesi istenen resimler için kullanılır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Image elementinin id'si                          |
    | value         | Image elementinin src'si                       |
'''
    def __init__(self,value = None,id = None)-> None: ...
from uix.elements._page import _page
class page(Element):
    '''
# page(value,id)
1. Page elementi. İçi boş bir ana div oluşturur. Sıfırdan bir sayfa oluşturmak için kullanılabilir. İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Page elementinin id'si                          |
    | value         | Page elementinin içeriği                       |
'''
    def __init__(self,value,id = None)-> None: ...
from uix.elements._video import _video
class video(Element):
    """
# video(id,loop,autoplay,muted)
1. Html'de video elementine karşılık gelir. İçerisine source elementleri eklenerek kullanılır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Video elementinin id'si                          |
    | loop          | Video elementinin sürekli oynatılması            |
    | autoplay      | Video elementinin otomatik oynatılması           |
    | muted         | Video elementinin sesinin kapatılması            |
"""
    def __init__(self, value = None, id = None,loop="true", autoplay="true", muted="true", src=None)-> None: ...
from uix.elements._thead import _thead
class thead(Element):
    '''
# thead(value,id = None)
1. Tablonun başlık kısmı. Tablonun içerisine başlık eklemek için kullanılır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | thead elementinin id'si                          |
    | value         | thead elementinin içeriği                       |
'''
    def __init__(self,value = None, id = None, name = None)-> None: ...
from uix.elements._td import _td
class td(Element):
    '''
# td(value,id = None)
1. Td elementi. Html'deki td elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Td elementinin id'si                          |
    | value         | Td elementinin içeriği                       |
'''
    def __init__(self, value = None, id = None)-> None: ...
from uix.elements._datalist import _datalist
class datalist(Element):
    '''
# datalist(value,id = "myDataList")
1. Datalist elementi. Html'deki datalist elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Datalist elementinin id'si                          |
    | value         | Datalist elementinin içeriği                       |
'''
    def __init__(self, value=None, id=None)-> None: ...
from uix.elements._table import _table
class table(Element):
    '''
# table(value,id = None)
1. Table elementi. Html'deki table elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Table elementinin id'si                          |
    | value         | Table elementinin içeriği                       |
'''
    def __init__(self,value = None, id = None)-> None: ...
from uix.elements._dialog import _dialog
class dialog(Element):
    '''
# dialog(value,id = None, is_clickable_anywhere = True)

1. Dialog elementi. Bir dialog penceresi açar.

    | attr                  | desc                                              |
    | :-------------------- | :------------------------------------------------ |
    | id                    | Dialog elementinin id'si                          |
    | value                 | Dialog elementinin içeriği                       |
    | close_on_outside      | Dışarı tıklanınca kapanma özelliği               |
'''
    def __init__(self,value = None,id = None, close_on_outside = True)-> None: ...
from uix.elements._tr import _tr
class tr(Element):
    '''
# tr(value,id = None)
1. Html'deki tr elementine karşılık gelir. Tablo içerisinde satır oluşturmak için kullanılır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Tr elementinin id'si                          |
    | value         | Tr elementinin içeriği                       |
'''
    def __init__(self,value = None, id = None,name = None)-> None: ...
from uix.elements._label import _label
class label(Element):
    '''
# label(value,id,tabindex = -1,usefor = None)
1. Label elementi. Bir input elementine ait label elementi için kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Labelin id'si                          |
    | value         | Label içeriği                       |
    | tabindex      | Labelin tabindex'i. Varsayılan değer: -1. Değer -1 ise tab ile focuslanamaz. |
    | usefor        | Labelin kullanıldığı input elementinin id'si |
'''
    def __init__(self,value= None,id = None, tabindex = -1, usefor = None)-> None: ...
from uix.elements._option import _option
class option(Element):
    '''
# option(value,id)
1. Temel option elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Option elementinin id'si                          |
    | value         | Option elementinin içeriği                       |
    | selected      | Optionun varsayılan olarak seçili olucak değeri tanımlar. |
    | disabled      | Optionun etkinliğini kapatır. |
'''
    def __init__(self,value = None,id = None)-> None: ...
from uix.elements._input import _input
class input(Element):
    '''
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
    | list          | Input elementinin list'i                        |
'''
    def __init__(self,value = None,id = None,type='text',name=None,placeholder="",required=False,list=None)-> None: ...
from uix.elements._orderedlist import _orderedlist
class orderedlist(Element):
    '''
# orderedlist(value,id)
1. Sıralı liste elementi. Listeye eleman eklemek için listitem elementi kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Sıralı Listenin id'si                          |
    | value         | Liste içeriği                       |
'''
    def __init__(self, value=None, id=None)-> None: ...
from uix.elements._header import _header
class header(Element):
    '''
# header(value,id = None)
1. Header elementi. Html header elementine karşılık gelir. İçerisine eklenen elemanlar, kullanıldığı divin en üstünde yer alır.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Header elementinin id'si                          |
    | value         | Header elementinin içeriği                       |
'''
    def __init__(self,value = None, id = None)-> None: ...
from uix.elements._container import _container
class container(Element):
    '''
# container(value,id = None)
1. Container elementi. İçerisine elemanlar eklenerek kullanılır. Eklenen elemanları yatayda ve dikeyde ortalar.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Container elementinin id'si                          |
    | value         | Container elementinin içeriği                       |
'''
    def __init__(self,value,id = None)-> None: ...
from uix.elements._radio import _radio
class radio(Element):
    """
# radio(value,id,name)
1. Temel HTML radio elementi.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | radio elementinin id'si                          |
    | value         | radio elementinin değeri                       |
    | name          | radio elementinin bağlı olduğu grubun adı       |
"""
    def __init__(self,value = None, id = None,name = None)-> None: ...
from uix.elements._link import _link
class link(Element):
    '''
# link(value,id,href,title,target)
1. Link elementi. Html'deki a elementine karşılık gelir. Sayfaya bağlantı eklemek için kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Link elementinin id'si                            |
    | value         | Link elementinin yazısı                           |
    | href          | Link elementinin href'i                           |
    | title         | Kullanıcı linkin üzerine geldiğinde göreceği yazı |
    | target        | Linkin açılacağı pencere seçeneği                 |
'''
    def __init__(self,value,id = None, href = None, title="", target="")-> None: ...
from uix.elements._progress import _progress
class progress(Element):
    """
# progress(value,id,max)
1. Progress bir input elementidir.
| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Progress elementinin id'si                        |
| value         | Progress elementinin değeri                       |
| max           | Progress'in maksimum değeri                       |
"""
    def __init__(self,value = 0,id = None, max = 100)-> None: ...
from uix.elements._grid import _grid
class grid(Element):
    '''
# grid(value,id,columns,rows)
1. Grid elementi. Grid özelliğinde bir div oluşturur. column ve row değerleri girilerek içerisindeki elemanlar grid özelliğine göre konumlandırılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Grid elementinin id'si                          |
    | value         | Grid elementinin içeriği                       |
    | columns       | Grid elementinin sütun değerlerini belirler. Örneğin: "150px 600px" |
    | rows          | Grid elementinin satır değerlerini belirler. Örneğin: "150px 600px" |
'''
    def __init__(self,value,id = None, columns = None, rows = None)-> None: ...
from uix.elements._div import _div
class div(Element):
    '''
# div(value,id = None)
1. Div elementi. Html'deki div elementine karşılık gelir. İçerisine elemanlar eklenerek kullanılır.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Div elementinin id'si                          |
    | value         | Div elementinin içeriği                       |
'''
    def __init__(self,value = None,id = None)-> None: ...
