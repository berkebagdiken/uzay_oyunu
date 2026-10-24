# Ad Soyad: Berke Bağdiken
# Hafta 5 Testleri: Dekoratörler

from uzay_oyunu.dekoratorler import sure_olc


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