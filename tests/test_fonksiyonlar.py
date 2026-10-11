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