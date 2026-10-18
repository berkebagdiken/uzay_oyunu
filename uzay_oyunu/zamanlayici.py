# Ad Soyad: Berke Bağdiken
# Hafta 4 - Bonus (+10): Zamanlayıcı Üreteci ve Meşgul Bekleme

from collections.abc import Generator
import time


def zamanlayici(aralik: float) -> Generator[float, None, None]:
    """Belirtilen saniye aralığında tetiklenen zamanlayıcı üreteci."""
    son = time.perf_counter()
    while True:
        simdi = time.perf_counter()
        if simdi - son >= aralik:
            yield simdi
            son = simdi


def tik_tak_calistir(toplam_sure: float = 10.0):
    """10 saniye boyunca her 2 saniyede 'tik', her 5 saniyede 'tak' yazar."""
    baslangic = time.perf_counter()
    son_tik = baslangic
    son_tak = baslangic

    print("Zamanlayıcı başlatıldı...")
    while time.perf_counter() - baslangic < toplam_sure:
        simdi = time.perf_counter()
        if simdi - son_tik >= 2.0:
            print(f"[{simdi - baslangic:.1f}s] tik")
            son_tik = simdi
        if simdi - son_tak >= 5.0:
            print(f"[{simdi - baslangic:.1f}s] tak")
            son_tak = simdi

    print("Süre tamamlandı.")


# MEŞGUL BEKLEME (BUSY WAITING) VE time.sleep FARKI:
# 1. Neden Meşgul Beklemedir?
# 'while' döngüsü süre dolana kadar CPU çekirdeğini hiç bırakmadan sürekli sorgulama yapar (spin-lock).
# Bu durum işlemci çekirdeğini %100 yük altına sokar ve gereksiz enerji tüketir.
#
# 2. time.sleep() ile Farkı:
# time.sleep() çağrıldığında işletim sistemi iş parçacığını (thread) askıya alır ve CPU'yu
# diğer işlemlere devreder. Süre dolunca uyandırır; böylece CPU tüketimi %0 düzeyinde kalır.

if __name__ == "__main__":
    tik_tak_calistir(10.0)