## UIX Element Resources and Static File Serving

This document provides detailed information on how to use the `uix.app.serve_module_static_files(__file__)` function, as well as how to register scripts and styles for an `Element` class using the `register_script` and `register_style` methods.

## 1. `uix.app.serve_module_static_files`

#### Overview

The `uix.app.serve_module_static_files` function is used to serve static files associated with a specific module. This function is particularly useful when you have resources like JavaScript, CSS, or images that need to be accessible via a specific route in your application.

#### Usage

To serve static files for a module, call `uix.app.serve_module_static_files` with the `__file__` argument in your module:

```python
import uix
from ..core.element import Element

uix.app.serve_module_static_files(__file__)
```

By default, this function looks for static files in a directory named `_public` located in the same directory as the module file. However, you can specify a different directory name by passing it as a second argument:

```python
uix.app.serve_module_static_files(__file__, static_dirname="custom_static")
```

#### Example Scenario

Suppose you have a module that includes static resources (like stylesheets or JavaScript files) stored in a `_public` directory. By calling `uix.app.serve_module_static_files(__file__)`, these resources will be automatically served, allowing them to be accessed via a URL route in your application.

If your static files are stored in a different directory, such as `custom_static`, you can specify this directory as the `static_dirname`:

```python
uix.app.serve_module_static_files(__file__, static_dirname="custom_static")
```

#### Warning: Served Route is Under the Module Name

It's important to note that the static files will be served under a URL route that includes the module name. For example, if your module is named `my_module` and you have a CSS file named `test.css`, it will be accessible via the following route:

```
/my_module/test.css
```

## 2. `Element.register_script` and `Element.register_style`

### Overview

The `register_script` and `register_style` methods are class methods of the `Element` class that allow you to register JavaScript and CSS resources for your elements. These methods can be used to include custom scripts and styles that are specific to an element.

### Methods

#### `register_script`

- **Description**: Registers a JavaScript resource for the element.
- **Parameters**:
  - `key`: `str` - A unique identifier for the script.
  - `content`: `str` - The script content or URL if `is_url` is `True`.
  - `is_url`: `bool`, optional - Set to `True` if `content` is a URL. Default is `False`.
  - `before_main`: `bool`, optional - Set to `True` if the script should be loaded before the main script. Default is `False`.
  - `defer`: `bool`, optional - Set to `True` if the script should be deferred. Default is `False`.
  - `module`: `bool`, optional - Set to `True` if the script should be treated as a module. Default is `False`.
  - `async_load`: `bool`, optional - Set to `True` if the script should be loaded asynchronously. Default is `False`.

#### `register_style`

- **Description**: Registers a CSS resource for the element.
- **Parameters**:
  - `key`: `str` - A unique identifier for the style.
  - `content`: `str` - The CSS content or URL if `is_url` is `True`.
  - `is_url`: `bool`, optional - Set to `True` if `content` is a URL. Default is `False`.

### Example Usage

```python
import uix
from ..core.element import Element

uix.app.serve_module_static_files(__file__)

js_content = """
const docs = "content";
"""

js_content1 = """
const docs2 = "content2";
"""

style_content = """
. css_class {
    color: green;
}
"""

def register_resources(cls):
    cls.register_script("script_key", js_content)
    cls.register_script("script_key1", js_content1)
    cls.register_script("cdn", "cdn.com/library.js", is_url=True)
    cls.register_script("cdn1", "cdn.com/library1.js", is_url=True, before_main=True)
    cls.register_script("cdn2", "cdn.com/library2.js", is_url=True, module=True)
    cls.register_style("dialog_style", style_content)
    cls.register_style("dialog_style", "/_basic_alert/_basic_alert.css", is_url=True)
    return cls

@register_resources
class ClassTest(Element):
    def __init__(self, value=None, id=None):
        super().__init__(id=id, value=value)

        with self:
            pass
```