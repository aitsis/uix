#Element class'ı bg fonksiyonu kullanım örneği.
import uix
from uix.elements import container, border, row

def _root():
    with container() as main:
        with row():
            border().size(100,100).bg("red")
            border().size(100,100).bg("green")
            border().size(100,100).bg("blue")
    return main


uix.start(ui = _root(), config = {"debug":True})