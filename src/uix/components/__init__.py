
import sys
import os
from types import ModuleType

all_by_module = {}

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and file.startswith("_") and file != "__init__.py":
        module_name = file[1:-3]
        all_by_module["uix.components._"+module_name] = [module_name]


object_origins = {}
for module, items in all_by_module.items():
    for item in items:
        object_origins[item] = module

class module(ModuleType):
    """Automatically import objects from the modules."""

    def __getattr__(self, name):
        if name in object_origins:
            module = __import__(object_origins[name], None, None, [name])
            for extra_name in all_by_module[module.__name__]:
                setattr(self, extra_name, getattr(module, extra_name))
            return getattr(module, name)
        
        return ModuleType.__getattribute__(self, name)

    def __dir__(self):
        """Just show what we want to show."""
        result = list(new_module.__all__)
        result.extend(
            (
                "__file__",
                "__doc__",
                "__all__",
                "__docformat__",
                "__name__",
                "__path__",
                "__package__",
                "__version__",
            )
        )
        return result

old_module = sys.modules["uix.components"]
new_module = sys.modules["uix.components"] = module("uix.components")
__version__ = "0.1.0"
new_module.__dict__.update(
    {
        "__file__": __file__,
        "__package__": "uix.components",
        "__path__": __path__,
        "__doc__": __doc__,
        "__version__": __version__,
        "__all__": tuple(object_origins),
        "__docformat__": "restructuredtext en",
    }
)