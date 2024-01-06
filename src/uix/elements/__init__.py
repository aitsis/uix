import sys
import os
from types import ModuleType
import importlib
modules = []
__all__ = modules
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and file.startswith("_") and file != "__init__.py":
        module_name = file[1:-3]
        modules.append(module_name)


def __getattr__(name):
    print("Imported: __getattr__ name:", name)
    print("modules = ", modules)
    if name in modules:
        module = importlib.import_module(f"uix.elements._{name}")
        print("Imported: Module =", module)
        attr = getattr(module, name)
        print("Imported: attr =", attr)
        return attr
    raise AttributeError(f"module {__name__} has no attribute {name}")
    

def __dir__():
    """Just show what we want to show."""
    print("Imported: __dir__")
    result = list(modules)
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