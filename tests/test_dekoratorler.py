# Ad Soyad: Berke Bağdiken
# Hafta 5 Testleri: Dekoratörler

import functools
from uzay_oyunu.dekoratorler import say, sure_olc 


def test_sure_olc(capsys):
    @sure_olc
    def ornek_fonksiyon(a: int, carpan: int = 2) -> int:
        """Bu fonksiyonun açıklama metnidir."""
        return a * carpan

    # 1. Test: Sonuç değişmeden dönüyor mu?
    sonuc = ornek_fonksiyon(5)
    assert sonuc == 10

    # 2. Test: Adlı argümanlarla (kwargs) çağrı çalışıyor mu?
    sonuc_kwargs = ornek_fonksiyon(4, carpan=3)
    assert sonuc_kwargs == 12

    # 3. Test: __name__ ve __doc__ korunuyor mu?
    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Bu fonksiyonun açıklama metnidir."

    # Konsol çıktısı format kontrolü ("ad: 0.0123 sn")
    yakalanan = capsys.readouterr().out
    assert "ornek_fonksiyon:" in yakalanan
    assert "sn" in yakalanan

def test_say_ve_dekorator_sirasi():
    # 1. Durum: Yalnızca @say
    @say
    def fib1(n: int) -> int:
        if n < 2:
            return n
        return fib1(n - 1) + fib1(n - 2)

    assert fib1(20) == 6765
    assert fib1.cagri == 21891

    # 2. Durum: @say üstte, @lru_cache altta
    @say
    @functools.lru_cache(maxsize=None)
    def fib2(n: int) -> int:
        if n < 2:
            return n
        return fib2(n - 1) + fib2(n - 2)

    assert fib2(20) == 6765
    assert fib2.cagri == 39

    # 3. Durum: @lru_cache üstte, @say altta
    @functools.lru_cache(maxsize=None)
    @say
    def fib3(n: int) -> int:
        if n < 2:
            return n
        return fib3(n - 1) + fib3(n - 2)

    assert fib3(20) == 6765
    assert fib3.__wrapped__.cagri == 21