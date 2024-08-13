## UIX Eleman Kaynakları ve Statik Dosya Sunumu

Bu belge, `uix.app.serve_module_static_files(__file__)` fonksiyonunun nasıl kullanılacağı ve bir `Element` sınıfı için `register_script` ve `register_style` metodlarını nasıl kaydedeceğinize dair ayrıntılı bilgiler sağlar.

## 1. `uix.app.serve_module_static_files`

#### Genel Bakış

`uix.app.serve_module_static_files` fonksiyonu, belirli bir modüle ait statik dosyaları sunmak için kullanılır. Bu fonksiyon, JavaScript, CSS veya resimler gibi kaynakları belirli bir route üzerinden erişilebilir hale getirmek istediğinizde özellikle faydalıdır.

#### Kullanım

Bir modül için statik dosyaları sunmak için, modülünüzde `__file__` argümanını kullanarak `uix.app.serve_module_static_files` fonksiyonunu çağırabilirsiniz:

```python
import uix
from ..core.element import Element

uix.app.serve_module_static_files(__file__)
```

Varsayılan olarak, bu fonksiyon, modül dosyasının bulunduğu dizinde `_public` adında bir dizin arar. Ancak, farklı bir dizin adı belirtmek isterseniz, bunu ikinci bir argüman olarak geçirebilirsiniz:

```python
uix.app.serve_module_static_files(__file__, static_dirname="custom_static")
```

#### Örnek Senaryo

Diyelim ki statik kaynakları (örneğin stil dosyaları veya JavaScript dosyaları) `_public` dizininde bulunan bir modülünüz var. `uix.app.serve_module_static_files(__file__)` fonksiyonunu çağırarak, bu kaynaklar otomatik olarak sunulacak ve uygulamanızda bir URL route'u üzerinden erişilebilir hale gelecektir.

Eğer statik dosyalarınız farklı bir dizinde saklanıyorsa, örneğin `custom_static` gibi, bu dizini `static_dirname` olarak belirtebilirsiniz:

```python
uix.app.serve_module_static_files(__file__, static_dirname="custom_static")
```

#### Uyarı: Sunulan Route Modül Adı Altında Olur

Dikkat edilmesi gereken önemli bir nokta, statik dosyaların, URL route'unda modül adını içeren bir yol altında sunulacak olmasıdır. Örneğin, modülünüzün adı `my_module` ise ve `test.css` adında bir CSS dosyanız varsa, bu dosyaya şu rota üzerinden erişebilirsiniz:

```
/my_module/test.css
```

## 2. `Element.register_script` ve `Element.register_style`

### Genel Bakış

`register_script` ve `register_style` metodları, `Element` sınıfının sınıf metodları olup, elemanlarınız için JavaScript ve CSS kaynaklarını kaydetmenizi sağlar. Bu metodlar, belirli bir elemana özgü özel script ve stilleri dahil etmek için kullanılabilir.

### Metodlar

#### `register_script`

- **Açıklama**: Eleman için bir JavaScript kaynağı kaydeder.
- **Parametreler**:
  - `key`: `str` - Script için benzersiz bir tanımlayıcı.
  - `content`: `str` - Script içeriği veya `is_url` `True` ise URL.
  - `is_url`: `bool`, isteğe bağlı - `content` bir URL ise `True` olarak ayarlanır. Varsayılan `False`dur.
  - `before_main`: `bool`, isteğe bağlı - Script'in ana script'ten önce yüklenmesi gerekiyorsa `True` olarak ayarlanır. Varsayılan `False`dur.
  - `defer`: `bool`, isteğe bağlı - Script'in geciktirilmesi gerekiyorsa `True` olarak ayarlanır. Varsayılan `False`dur.
  - `module`: `bool`, isteğe bağlı - Script'in bir modül olarak ele alınması gerekiyorsa `True` olarak ayarlanır. Varsayılan `False`dur.
  - `async_load`: `bool`, isteğe bağlı - Script'in asenkron olarak yüklenmesi gerekiyorsa `True` olarak ayarlanır. Varsayılan `False`dur.

#### `register_style`

- **Açıklama**: Eleman için bir CSS kaynağı kaydeder.
- **Parametreler**:
  - `key`: `str` - Stil için benzersiz bir tanımlayıcı.
  - `content`: `str` - Stil içeriği veya `is_url` `True` ise URL.
  - `is_url`: `bool`, isteğe bağlı - `content` bir URL ise `True` olarak ayarlanır. Varsayılan `False`dur.

### Örnek Kullanım

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
