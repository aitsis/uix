
md_text = """
# Welcome to uix

You can write an ui app like that:

Example Code:

```python
import uix

from uix.elements import div

main = div("Hello World!").style("font-size","30px")

uix.start(ui = main)
```
"""

import uix
from uix.elements import md

start_example = md(md_text)
if __name__ == "__main__":
    uix.start(ui = start_example, debug=True)