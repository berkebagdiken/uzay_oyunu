# Ad Soyad: Berke Bağdiken
# Hafta 3 - Görev 5 Testleri

from uzay_oyunu.araclar import en_bagli_gezegenler, hamle_sayaci, sure_olc


def test_hamle_sayaci():
    sayac1 = hamle_sayaci()
    assert sayac1() == 1
    assert sayac1() == 2
    assert sayac1() == 3

    # Yeni sayaç birbirinden bağımsız olmalı
    sayac2 = hamle_sayaci()
    assert sayac2() == 1


def test_en_bagli_gezegenler():
    galaksi = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius"],  # 2 bağlantı
            "centauri": ["dünya", "orion"],  # 2 bağlantı
            "sirius": ["dünya", "orion", "kara_delik"],  # 3 bağlantı
            "orion": ["centauri", "sirius"],  # 2 bağlantı
            "kara_delik": ["sirius"],  # 1 bağlantı
        },
    }
    sonuc = en_bagli_gezegenler(galaksi)
    # Sirius (3) > Centauri (2, C) > Dünya (2, D) > Orion (2, O) > Kara Delik (1)
    beklenen = ["sirius", "centauri", "dünya", "orion", "kara_delik"]
    assert sonuc == beklenen


def test_sure_olc():
    def topla(a, b):
        return a + b

    olcen_topla = sure_olc(topla)
    assert olcen_topla(3, 5) == 8