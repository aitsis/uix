import json
import os
from ..app import error,log
class Locale:
    def __init__(self,locales_path):
        self.locales_path = locales_path
        self.lang = None

    def load(self,lang):
        for filename in os.listdir(self.locales_path):
            if filename.endswith(".json"):
                if filename[:-5] == lang:
                    with open(os.path.join(self.locales_path, filename), 'r') as f:
                        self.lang = lang
                        self.data = json.load(f)
                        log("Locale loaded: " + lang)
                        return True
        if lang != "en":
            error("Locale not found: " + lang)
        return False
        
    def __getitem__(self, key):
        if self.lang is None:
            return key
        else:
            if key in self.data:
                return self.data[key]
            else:
                error("Locale key not found: " + key)
            return key