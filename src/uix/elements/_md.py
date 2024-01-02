import uix
from ..core.element import Element
print("Imported: md2")
uix.html.add_header_item("md2_js", '<script src="https://cdn.jsdelivr.net/npm/markdown-it@14.0.0/dist/markdown-it.min.js"></script>')
uix.html.add_header_item("md2_hljs", '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>')
#uix.html.add_header_item("md2_css",'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">')
uix.html.add_header_item("md2_css",'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">')
uix.html.add_script("md2", beforeMain = False, script =
'''
    var md = window.markdownit({
        highlight: function (str, lang) {
            if (lang && hljs.getLanguage(lang)) {
                try {
                    return '<pre class="hljs"><code>' +
                           hljs.highlight(str, { language: lang, ignoreIllegals: true }).value +
                           '</code></pre>';
                } catch (__) {}
            }

            return '<pre class="hljs"><code>' + md.utils.escapeHtml(str) + '</code></pre>';
        }
    });
    event_handlers["md2-change-md"] = function(id, value, event_name){
        document.getElementById(id).innerHTML = md.render(value);
    }
''')
uix.html.add_css("md2_css_style", style = '''
    <style>
        .hljs {
            color: #ddd;
            background: #000
        }
        pre.hljs {
            background-color: #000 !Important;
        }
        /* Optional: Style for inline code */
        code {
            padding: 0.2em 0.4em;
            border-radius: 3px;
        }
    </style>
''')

class md(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)

    def bind(self, session, only_children=False):
        if self.id is None:
            self.id = "md2_" + str(session.next_id())
        super().bind(session, only_children)
        self.session.queue_for_send(self.id, self.value, "md2-change-md")
    
    def send_value(self, value):
        self.session.send(self.id, value, "md2-change-md")



title = "Markdown"

description = '''
# md(value,id)
1. Markdown elementi. Markdown dilinde yazılmış metni html'e çevirir.
    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | id            | Markdown elementinin id'si                          |
    | value         | Markdown elementinin içeriği                       |
'''

sample = """
    
    md('''# Markdown!
    ```python
    from uix.elements import div

    def hello_world_example():
        main = div("Hello World!").style("font-size","30px")
        return main
    ```
                ''')

"""