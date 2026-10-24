# Ad Soyad: Berke Bağdiken
# Hafta 5 - Dekoratörler Modülü

import functools
import time
from typing import Any, Callable


def sure_olc(fonksiyon: Callable) -> Callable:
    """Fonksiyonun çalışma süresini time.perf_counter() ile ölçüp ekrana yazdıran dekoratör."""

    @functools.wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"{fonksiyon.__name__}: {gecen_sure:.4f} sn")
        return sonuc

    return sarmalayici

def say(fonksiyon: Callable) -> Callable:
    """Çağrı sayısını fonksiyonun 'cagri' niteliğinde sayan dekoratör."""

    @functools.wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        sarmalayici.cagri += 1
        return fonksiyon(*args, **kwargs)

    sarmalayici.cagri = 0
    return sarmalayici

def log_cagri(fonksiyon: Callable) -> Callable:
    """Her çağrıdan önce fonksiyon adını ve argümanlarını,

    çağrıdan sonra ise dönüş değerini ekrana yazdıran dekoratör.
    """

    @functools.wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        arg_listesi = [repr(a) for a in args] + [
            f"{k}={v!r}" for k, v in kwargs.items()
        ]
        arg_metni = ", ".join(arg_listesi)
        print(f"-> {fonksiyon.__name__}({arg_metni})")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"<<- {fonksiyon.__name__} {sonuc!r}")
        return sonuc

    return sarmalayici