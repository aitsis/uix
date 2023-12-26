import json
import os
from ..app import error,log, config
import threading
from .session import context

def set_lang(lang):
    if not hasattr(context, "session"):
        error("No session")
        return
    if context.session.locale is None:
        if "locales_path" in config and config["locales_path"] is not None:
            context.session.locale = Locale(config["locales_path"])
        else:
            error("No locales_path in config"
                  )
    context.session.locale.load(lang.lower())

def T(text):
    if hasattr(context, "session"):
        locale = context.session.locale
    else:
        locale = None

    if locale is None:
        return text
    else:
        return locale[text]
    
class Locale:
    def __init__(self,locales_path):
        self.locales_path = locales_path
        self.lang = "en"

    def load(self,lang):
        if lang == "en":
            self.lang = "en"
            return True
        
        for filename in os.listdir(self.locales_path):
            if filename.endswith(".json"):
                if filename[:-5] == lang:
                    with open(os.path.join(self.locales_path, filename), 'r') as f:
                        self.lang = lang
                        self.data = json.load(f)
                        log("Locale loaded: " + lang)
                        return True
        return False
        
    def __getitem__(self, key):
        if self.lang is None or self.lang == "en":
            return key
        else:
            if key in self.data:
                return self.data[key]
            else:
                error("Locale key not found: " + key)
            return key