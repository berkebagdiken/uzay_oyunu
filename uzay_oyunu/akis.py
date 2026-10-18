# Ad Soyad: Berke Bağdiken
# Hafta 4 - Akış ve Üreteç Modülü

from collections.abc import Generator
import functools
import itertools
from pathlib import Path
from typing import Any, Callable


def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayı dizisi üreten üreteç (0, 1, 1, 2, 3, 5, ...)."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her çağrıda yakıtı tüketim miktarı kadar azaltıp kalanı üreten üreteç.
    
    Yakıt 0'a ulaştığında durur.
    """
    kalan = yakit
    while kalan > 0:
        kalan = max(0, kalan - tuketim)
        yield kalan     
def satirlari_oku(yol: str | Path) -> Generator[str, None, None]:
    """Dosyayı satır satır okur; boş satırları ve # ile başlayan yorumları atlar."""
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz


def ayristir(
    satirlar: Generator[str, None, None],
) -> Generator[tuple[str, str, int], None, None]:
    """Her satırdan (kaynak, hedef, yakit) demeti üreten tembel üreteç."""
    for satir in satirlar:
        temiz = satir.replace("->", " ").replace(">", " ")
        parcalar = temiz.split()
        if len(parcalar) >= 3:
            kaynak, hedef, yakit = parcalar[0], parcalar[1], int(parcalar[2])
            yield (kaynak, hedef, yakit)


def uzun_yolculuklar(
    kayitlar: Generator[tuple[str, str, int], None, None],
    esik: int,
) -> Generator[tuple[str, str, int], None, None]:
    """Yakıt tüketimi belirtilen eşikten büyük olan yolculukları süzen üreteç."""
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit