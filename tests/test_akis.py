# Ad Soyad: Berke Bağdiken
# Hafta 4 Testleri

import itertools
import pytest
from uzay_oyunu.akis import fibonacci, yakit_gostergesi, satirlari_oku, ayristir, uzun_yolculuklar


def test_fibonacci_yollari_ve_tek_kullanimlik():
    # 1. Yol: next() ile ilk 3 değer
    g1 = fibonacci()
    assert (next(g1), next(g1), next(g1)) == (0, 1, 1)

    # 2. Yol: itertools.islice ile ilk 12 değer
    ilk_12 = list(itertools.islice(fibonacci(), 12))
    assert ilk_12 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # 3. Yol: itertools.takewhile ile 100'den küçük değerler
    kucuk_100 = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
    assert kucuk_100 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # Üretecin tek kullanımlık olduğunu gösterme:
    g2 = fibonacci()
    parca1 = list(itertools.islice(g2, 3))  # [0, 1, 1] çeker
    parca2 = list(itertools.islice(g2, 3))  # [2, 3, 5] çeker (aynı üreteç kaldığı yerden devam eder)
    assert parca1 != parca2
    assert parca1 == [0, 1, 1]
    assert parca2 == [2, 3, 5]

def test_yakit_gostergesi_ve_stopiteration():
    # PDF'teki örnek: list(yakit_gostergesi(100, 30)) -> [70, 40, 10, 0]
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]

    # StopIteration davranışı testi
    g = yakit_gostergesi(10, 10)
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)
def test_seyir_boru_hatti(tmp_path):
    # Test ortamı için geçici dosya oluşturma
    test_dosyasi = tmp_path / "seyir.txt"
    test_dosyasi.write_text(
        "dünya -> sirius 12\n"
        "sirius -> orion 8\n"
        "orion -> centauri 15\n"
        "#bakım molası\n"
        "centauri -> orion 15\n"
        "orion > sirius 8\n"
        "sirius -> kara_delik 30\n",
        encoding="utf-8",
    )

    # 1. Aşama doğrulaması: Toplam yakıt 88 olmalı
    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(test_dosyasi)))
    assert toplam_yakit == 88

    # 2. Aşama doğrulaması: Yakıtı 10'dan büyük hedefler
    kayitlar = ayristir(satirlari_oku(test_dosyasi))
    uzun_hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert uzun_hedefler == ["sirius", "centauri", "orion", "kara_delik"]