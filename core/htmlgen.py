import re

class HTMLGen:
    def __init__(self):
        self.default_header_items = {
            'meta-charset': '<meta charset="UTF-8">',
            'meta-viewport': '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            'socket.io': '<script src="js/socket.io.min.js"></script>',
            'style': '<link rel="stylesheet" href="style.css">',
            'favicon': '<link rel="icon" href="https://ai.ait.com.tr/wp-content/uploads/cropped-favicon_aiait-32x32.png" sizes="32x32" />'
        }
        self.header_items = {}
        self.default_script_sources = {"main": "<script src='js/main.js'></script>"}
        self.script_sources = {}
        self.scripts = {}
        self.styles = {}

    def add_header_item(self, id, item):
        self.header_items.setdefault(id, item)
        
    def add_script_source(self, id, script):
        self.script_sources.setdefault(id, script)

    def add_script(self, id, script):
        self.scripts.setdefault(id, script)

    def add_css(self, id, style):
        self.styles.setdefault(id, style)

    def minify_js(self, js_code):
        return re.sub(r'\s+', ' ', re.sub(r'//.*?\n|/\*.*?\*/', '', js_code)).strip()

    def minify_css(self, css_code):
        return re.sub(r'\s+', ' ', re.sub(r'/\*.*?\*/', '', css_code)).strip()

    def minify_html(self, html_code):
        return re.sub(r'>\s+<', '><', re.sub(r'<!--.*?-->', '', html_code)).strip()

    def get_index(self):
        # HTML BEGIN ------------------------------------------------------------
        index_str = '<!DOCTYPE html><html lang="en"><head>'
        # HEADER ITEMS ----------------------------------------------------------
        for key in self.default_header_items:
            index_str += self.default_header_items[key]
        for key in self.header_items:
            index_str += self.header_items[key]
        # STYLES ----------------------------------------------------------------
        for key in self.styles:
            index_str += '<style>'
            index_str += self.minify_css(self.styles[key])
            index_str += '</style>'
        index_str += '</head>'
        # BODY ------------------------------------------------------------------
        index_str += '<body>'
        index_str += "<div id='myapp'></div>"
        # SCRIPTS ---------------------------------------------------------------
        for key in self.default_script_sources:
            index_str += self.default_script_sources[key]
        for key in self.script_sources:
            index_str += self.script_sources[key]
        if len(self.scripts) > 0:
            for id in self.scripts:
                index_str += '<script>'
                index_str += self.minify_js(self.scripts[id])
                index_str += '</script>'
        index_str += '</body>'
        index_str += '</html>'
        index_str = self.minify_html(index_str)
        return index_str

    def get_minified_index(self):
        return self.minify_html(self.get_index())
