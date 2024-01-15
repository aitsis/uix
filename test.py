
import uix
from uix.elements import div, button, container, unorderedlist, listitem


def _root(data,component):
    if data == None:
        data = {}
    def create_tree(key,data,component):
        with unorderedlist(key):
            for key in data:
                if isinstance(data[key], dict):
                    create_tree(key,data[key],component)
                else:
                    with listitem(key):
                        component("")
    with div("") as main:
        create_tree("root",data,component)

    return main

data = {
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "key4": "value4",
        "key5": "value5",
        "key6": {
            "key7": "value7",
            "key8": "value8",
            "key9": "value9",
        }
    }
}
with unorderedlist("item") as _root2:
    listitem("item1")
    listitem("item2")
    listitem("item3")


uix.start(ui = _root(data,div), config = {"debug":True})