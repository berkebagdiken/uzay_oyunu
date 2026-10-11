# Ad Soyad: Berke Bağdiken
# Hafta 3 - Görev 5: Closure, Lambda ve Bonus

import time
from typing import Any, Callable


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında 1 artan bir sayaç fonksiyonu (closure) döndürür."""
    sayac = 0

    def artir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return artir


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre çoktan aza,

    bağlantı sayısı eşitse alfabetik sıraya göre sıralayarak döndürür.
    """
    baglantilar = galaksi.get("baglantilar", {})
    gezegenler = list(galaksi.get("gezegenler", []))

    # -len(baglantilar.get(g, [])) -> Azalan sıralama (en çok bağlantısı olan başa)
    # g                            -> Eşitlikte alfabetik sıralama (A'dan Z'ye)
    return sorted(
        gezegenler,
        key=lambda g: (-len(baglantilar.get(g, [])), g),
    )


def sure_olc(fonksiyon: Callable) -> Callable:
    """Verilen fonksiyonun çalışma süresini ölçen bir sarmalayıcı döndürür (Bonus +10)."""

    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"[{fonksiyon.__name__}] Çalışma süresi: {gecen_sure:.6f} saniye")
        return sonuc

    return sarmalayici