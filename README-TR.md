# uix

uix, Python kullanarak hem ön yüz (front-end) hem de arka yüz (back-end) web uygulamaları geliştirmek için tasarlanmış kapsamlı bir kütüphanedir. Bu kütüphane, temelde basit yapay zeka uygulamaları için arayüzler sunan [Gradio](https://github.com/gradio-app/gradio.git) kütüphanesinden  ilham alarak geliştirilmiştir. Daha kapsamlı bir çözüme ihtiyaç duyulduğunu fark ederek, uix AI'ın ötesine geçerek web geliştirme ihtiyaçlarının daha geniş bir yelpazesini destekleyecek şekilde genişletilmiştir.

Geliştirme sürecinde Streamlit ve NiceGui gibi diğer çeşitli platformlar değerlendirilmiştir. Her platformun güçlü yönleri ve sınırlamaları vardır, ancak hiçbiri ihtiyaçlarımızı tam olarak karşılamamıştır. Bu araştırma, tasarım kararlarımızı bilgilendirmenin yanı sıra, projemizin ana hedeflerinden biri olan önemli öğrenme fırsatları sağlamıştır.

uix'i keşfetmek ve uygulamada görmek için, uix-demo deposundan başlayabilirsiniz:

[uix-demo](https://github.com/aitsis/uix-demo.git)

**Mevcut Proje Hedefleri:**
- Kullanım kolaylığı ve erişilebilirliği sağlamak için dokümantasyonu genişletmek.
- Kütüphanenin yeteneklerini sergilemek için daha çeşitli örnek projeler oluşturup paylaşmak.

## Kurulum Gereksinimleri

uix'i kurmadan önce, sisteminizde aşağıdaki ön koşulların yüklü olduğundan emin olun:
- Python 3.8 veya daha yeni bir sürüm
- pip (Python paket yükleyicisi)

Python ve pip'i işletim sisteminizin paket yöneticisi aracılığıyla veya [python.org](https://www.python.org/) adresinden indirerek yükleyebilirsiniz.

## Kurulum Talimatları:

uix'i yerel olarak kurmak için depoyu klonlayın ve kurulum yapın:
```shell
git clone https://github.com/aitsis/uix.git
cd uix
pip install -r requirements.txt
pip install -e .
```
Bu kurulum yöntemi, kütüphaneyi bilgisayarınızdan global olarak erişilebilir hale getirir.

**Örnek Projeler İçin:**
```shell
git clone https://github.com/aitsis/uix-demo.git
```

**Ek Bileşenler İçin:**
```shell
git clone https://github.com/aitsis/uix-components.git
```

Bu araçları ve kaynakları sağlayarak, Python'u karmaşık web uygulamaları için kullanmak isteyen web geliştiricilere yönelik çok yönlü ve etkili bir ortam oluşturmayı amaçlamaktayız.