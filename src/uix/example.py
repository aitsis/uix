
md_text = """
# Welcome to uix

You can write an ui app like that:

Example Code:

```python
import uix

from uix.elements import div

def root():
    main = div("Hello World!").style("font-size","30px")
    return main

uix.start(ui = root)
```
"""

import uix
from uix.elements import md

def start_example():
    main = md(md_text)
    return main
if __name__ == "__main__":
    uix.start(ui = start_example)