# Ad Soyad: Berke Bağdiken
# Hafta 5 Testleri: Dekoratörler

import functools
from uzay_oyunu.dekoratorler import say, sure_olc , log_cagri
from uzay_oyunu.dekoratorler import sinirla, yakit_harca
from uzay_oyunu.dekoratorler import hafiza

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

def test_log_cagri(capsys):
    @log_cagri
    def yolculuk(hedef: str, hiz: int = 1) -> str:
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)
    assert sonuc == "orion hiz=3"

    cikti = capsys.readouterr().out
    assert "-> yolculuk('orion', hiz=3)" in cikti
    assert "<<- yolculuk 'orion hiz=3'" in cikti

import pytest
from uzay_oyunu.komutlar import KOMUTLAR, envanter, harita, komut, yardim


def test_komut_kayit_ve_hata():
    # Aynı komutun ikinci kez kaydedilmeye çalışılması tanım anında ValueError fırlatmalı
    with pytest.raises(ValueError, match="zaten kayıtlı"):
        @komut("yardim", "tekrarlanan komut")
        def yardim_kopya(durum):
            return ""

    # Dekoratörün fonksiyonu değiştirmeden döndürdüğünü doğrulama
    @komut("test_komutu", "test açıklaması")
    def ornek_komut(durum):
        return "çalıştı"

    assert ornek_komut({}) == "çalıştı"
    assert "test_komutu" in KOMUTLAR


def test_komutlar_yardim_harita_envanter():
    durum = {
        "konum": "dünya",
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "orion"],
            "sirius": ["dünya", "kara_delik"],
        },
        "credits": True,
        "engines": False,
        "copilot": True,
    }

    # 1. harita komutu testi
    assert harita(durum) == "centauri, sirius"

    # 2. envanter komutu testi
    assert envanter(durum) == "Sende: bol kredi, yetenekli bir pilot"

    # 3. yardim komutu testi
    yardim_metni = yardim(durum)
    assert "yardim komutları listeler" in yardim_metni
    assert "harita gidebileceğin gezegenleri gösterir" in yardim_metni
    assert "envanter eşyalarını gösterir" in yardim_metni

def test_sinirla_dekoratoru():
    # 1. Aralık içi normal çağrı
    assert yakit_harca(30) == 70

    # 2. Sınır değerleri (0 ve 100)
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0

    # 3. Aralık dışı değerler ve hata mesajı kontrolü
    with pytest.raises(
        ValueError, match="yakit_harca: 150 değeri 0-100 aralığında değil"
    ):
        yakit_harca(150)

    with pytest.raises(
        ValueError, match="yakit_harca: -5 değeri 0-100 aralığında değil"
    ):
        yakit_harca(-5)

def test_hafiza_bonusu_ve_lru_karsilastirma():
    # 1. lru_cache ile aynı sonuçları verdiğinin doğrulanması
    @hafiza()
    def fib_hafiza(n: int) -> int:
        if n < 2:
            return n
        return fib_hafiza(n - 1) + fib_hafiza(n - 2)

    @functools.lru_cache(maxsize=None)
    def fib_lru(n: int) -> int:
        if n < 2:
            return n
        return fib_lru(n - 1) + fib_lru(n - 2)

    for i in range(15):
        assert fib_hafiza(i) == fib_lru(i)

    # 2. maxsize dolduğunda en eski girdinin silinmesinin testi
    @hafiza(maxsize=2)
    def carp(x: int) -> int:
        return x * 10

    carp(1)
    carp(2)
    assert len(carp.onbellek) == 2

    carp(3)  # Kapasite doldu, en eski girdi olan (1) silinmeli
    assert len(carp.onbellek) == 2
    onbellek_argumanlari = [k[0][0] for k in carp.onbellek.keys()]
    assert 1 not in onbellek_argumanlari
    assert onbellek_argumanlari == [2, 3]