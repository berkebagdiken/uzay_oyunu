from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_metni_bos():
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_kismen_dolu():
    beklenen = "Sende: bol kredi, yetenekli bir pilot"
    assert envanter_metni(True, False, True) == beklenen


def test_hedef_menusu():
    hedefler = ["centauri", "sirius"]
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(hedefler) == beklenen
    # Ad Soyad: Berke Bağdiken
# Hafta 3 - Testler

import pytest
from uzay_oyunu.oyun import envanter_metni, galaksi_kur, hedef_menusu


def test_envanter_metni_bos():
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_kismen_dolu():
    beklenen = "Sende: bol kredi, yetenekli bir pilot"
    assert envanter_metni(True, False, True) == beklenen


def test_hedef_menusu():
    hedefler = ["centauri", "sirius"]
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(hedefler) == beklenen


def test_galaksi_kur_basarili():
    veri = {
        "gezegenler": ["dünya", "mars"],
        "baglantilar": {"dünya": ["mars"], "mars": []},
        "baslangic": "dünya",
        "yakit": 100,
    }
    g = galaksi_kur(**veri)
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100


def test_galaksi_kur_varsayilan_yakit():
    g = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g["yakit"] == 50


def test_galaksi_kur_gecersiz_baslangic():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "dünya")