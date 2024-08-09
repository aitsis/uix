import uix
from uuid import uuid4
from ..core.element import Element
print("Imported: md2")

md2_inline_script = '''
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
    };
'''

md2_style_inline = '''
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
'''

def register_resources(cls):
    cls.register_script("md2_js", "https://cdn.jsdelivr.net/npm/markdown-it@14.0.0/dist/markdown-it.min.js", is_url=True, before_main=True)
    cls.register_script("md2_js_highlight", "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js", is_url=True, before_main=True)
    cls.register_style("md2_css", "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css", is_url=True)
    cls.register_script("md2_inline", md2_inline_script, is_url=False, before_main=False)
    cls.register_style("md2_inline_css", md2_style_inline, is_url=False)
    return cls

@register_resources
class md(Element):
    def __init__(self,value:str = None,id:str = None):
        if id is None:
            id = str(uuid4())
        super().__init__(value, id = id)

    def init(self):
        self.session.queue_for_send(self.id, self.value, "md2-change-md")

    def send_value(self, value):
        self.session.send(self.id, value, "md2-change-md")
