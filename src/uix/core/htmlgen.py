import re
import os

class HTMLGen:
    def __init__(self):

        self.default_header_items = {
            'meta-charset': '<meta charset="UTF-8">',
            'meta-viewport': '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            'socket.io': '<script src="/static/socket.io.min.js"></script>',
            'style': '<link rel="stylesheet" href="/static/style.css">',
            'favicon': '<link rel="icon" href="/static/favicon_aiait-32x32.png" sizes="32x32" />',
            'fontawesome': '<link rel="stylesheet" href="/static/font-awesome/css/all.css" />'
        }
        self.header_items = {}
        self.default_script_sources = {"main": "<script src='/static/main.js'></script>"}
        self.script_sources_before_main = {}
        self.script_sources_after_main = {}
        self.scripts_before_main = {}
        self.scripts_after_main = {}
        self.styles = {}

    def add_header_item(self, id, item):
        self.header_items.setdefault(id, item)
        
    def add_script_source(self, id, script = None, beforeMain = True, localpath = None, _type = None):
        full_script = script
        if localpath is not None:
            full_script = os.path.join(os.path.dirname(os.path.abspath(localpath)), script)

        with open(full_script, 'r', encoding="utf-8") as file:
            data = {
                'file_data': file.read(),
                'script_type': _type
            }

        if beforeMain:
            self.script_sources_before_main.setdefault(id, data)
        else:
            self.script_sources_after_main.setdefault(id, data)

    def add_script(self, id, script = None, beforeMain = True):
        if beforeMain:
            self.scripts_before_main.setdefault(id, script)
        else:
            self.scripts_after_main.setdefault(id, script)

    def add_css(self, id, style):
        self.styles.setdefault(id, style)

    def add_css_file(self, path,localpath = None):
        full_path = path
        if localpath is not None:
            full_path = os.path.join(os.path.dirname(os.path.abspath(localpath)), path)
        with open(full_path, 'r') as file:
            id = os.path.basename(path)
            self.styles.setdefault(id, file.read())

    def minify_js(self, js_code):
        return re.sub(r'\s+', ' ', re.sub(r'//.*?\n|/\*.*?\*/', '', js_code)).strip()

    def minify_css(self, css_code):
        return re.sub(r'\s+', ' ', re.sub(r'/\*.*?\*/', '', css_code)).strip()
    
    def minify_html(self, html_code):
        return re.sub(r'>\s+<', '><', re.sub(r'<!--.*?-->', '', html_code)).strip()

    def generate(self, page_id = None):
        
        # HTML BEGIN ------------------------------------------------------------
        index_str = '<!DOCTYPE html><html lang="en" translate="no"><head>'
        # HEADER ITEMS ----------------------------------------------------------
        self.default_header_items.update(self.header_items)
        # for key in self.default_header_items:
        #     index_str += self.default_header_items[key]
        for key in self.default_header_items:
            index_str += self.default_header_items[key]
        # STYLES ----------------------------------------------------------------
        for key in self.styles:
            index_str += '<style>'
            index_str += self.minify_css(self.styles[key])
            index_str += '</style>'
        index_str += '</head>'
        # BODY ------------------------------------------------------------------
        index_str += '<body>'
        if page_id is not None:
            index_str += f"<div id='ait-uix' page-id={page_id}></div>"
        else:
            index_str += "<div id='ait-uix'></div>"
        # SCRIPTS ---------------------------------------------------------------
        # SCRIPT SOURCES --------------------------------------------------------
        for value in self.script_sources_before_main.values():
            opening_tag = '<script>' if value['script_type'] is None else f'<script type={value["script_type"]}>'
            index_str += opening_tag
            index_str += value['file_data']
            index_str += '</script>'
        # BEFORE MAIN SCRIPTS ---------------------------------------------------
        for id in self.scripts_before_main:
            index_str += '<script>'
            index_str += self.minify_js(self.scripts_before_main[id])
            index_str += '</script>'
        # MAIN SCRIPT -----------------------------------------------------------
        for key in self.default_script_sources:
            index_str += self.default_script_sources[key]
        # AFTER MAIN SCRIPTS ----------------------------------------------------
        for id in self.scripts_after_main:
            index_str += '<script>'
            index_str += self.minify_js(self.scripts_after_main[id])
            index_str += '</script>'
        # SCRIPT SOURCES --------------------------------------------------------
        for value in self.script_sources_after_main.values():
            opening_tag = '<script>' if value['script_type'] is None else f'<script type={value["script_type"]}>'
            index_str += opening_tag
            index_str += value['file_data']
            index_str += '</script>'
        # HTML END --------------------------------------------------------------
        index_str += '</body>'
        index_str += '</html>'
        index_str = self.minify_html(index_str)
        return index_str

    def get_minified_index(self):
        return self.minify_html(self.get_index())
