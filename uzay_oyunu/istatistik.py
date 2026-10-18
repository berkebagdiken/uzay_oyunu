# Ad Soyad: Berke Bağdiken
# Hafta 4 - Görev 5: map, filter, reduce ve partial

import functools
from typing import Callable


# 1. Soru: Gezegen Adlarının Büyük Harfli Listesi
def buyuk_harfli_map(gezegenler: list[str]) -> list[str]:
    """map() kullanarak gezegen adlarını büyük harfli liste olarak döndürür."""
    return list(map(str.upper, gezegenler))


def buyuk_harfli_liste_ureteci(gezegenler: list[str]) -> list[str]:
    """Liste üreteci (comprehension) kullanarak gezegen adlarını büyük harfe dönüştürür."""
    return [g.upper() for g in gezegenler]


# 2. Soru: En Az İki Bağlantısı Olan Gezegenler
def baglantisi_cok_filter(galaksi: dict) -> list[str]:
    """filter() kullanarak en az iki bağlantısı olan gezegenleri süzer."""
    baglantilar = galaksi.get("baglantilar", {})
    return list(
        filter(
            lambda g: len(baglantilar.get(g, [])) >= 2,
            galaksi.get("gezegenler", []),
        )
    )


def baglantisi_cok_liste_ureteci(galaksi: dict) -> list[str]:
    """Liste üreteci kullanarak en az iki bağlantısı olan gezegenleri süzer."""
    baglantilar = galaksi.get("baglantilar", {})
    return [
        g for g in galaksi.get("gezegenler", [])
        if len(baglantilar.get(g, [])) >= 2
    ]


# 3. Soru: Toplam Bağlantı Sayısı
def toplam_baglanti_reduce(galaksi: dict) -> int:
    """functools.reduce() kullanarak galaksideki toplam bağlantı sayısını hesaplar."""
    baglantilar = galaksi.get("baglantilar", {})
    return functools.reduce(
        lambda toplam, g: toplam + len(baglantilar.get(g, [])),
        galaksi.get("gezegenler", []),
        0,
    )


def toplam_baglanti_sum(galaksi: dict) -> int:
    """sum() ve üreteç ifadesi kullanarak galaksideki toplam bağlantı sayısını hesaplar."""
    baglantilar = galaksi.get("baglantilar", {})
    return sum(len(baglantilar.get(g, [])) for g in galaksi.get("gezegenler", []))


# 4. functools.partial ile Hızlı Yolculuk Fonksiyonu Türetme
def yolculuk(konum: str, hedef: str, hiz: int = 1) -> str:
    """İki nokta arasındaki yolculuk durumunu metin olarak üretir."""
    return f"{konum} -> {hedef} yolculuğu hız={hiz} ile tamamlandı."


# hiz=3 parametresi sabitlenmiş yeni fonksiyon
hizli_yolculuk: Callable[[str, str], str] = functools.partial(yolculuk, hiz=3)

# OKUNABİLİRLİK DEĞERLENDİRMESİ:
# Python'da (PEP 20 - Zen of Python) liste üreteçleri ve dahili 'sum()' fonksiyonu,
# map/filter/reduce üçlüsüne göre çok daha açık, doğrudan ve okunabilirdir.
# map ve filter fazladan lambda tanımları ve list() sarmalamaları gerektirirken;
# liste üreteçleri filtreleme ve dönüştürmeyi tek satırda doğal bir İngilizce sözdizimiyle sunar.