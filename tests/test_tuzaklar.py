# Ad Soyad: Berke Bağdiken
# Hafta 3 - Görev 4: Tuzak Testleri

from uzay_oyunu.oyun import yakit_ekle


def test_yakit_ekle_bagimsiz_depolar():
    """Her çağrıda depo verilmezse bağımsız yeni liste üretildiğini doğrular."""
    depo1 = yakit_ekle(10)
    assert depo1 == [10]

    # Hatalı depo=[] kalıbı kullanılsaydı depo2 [10, 20] döner ve test çökerdi
    depo2 = yakit_ekle(20)
    assert depo2 == [20]