# Ad Soyad: Berke Bağdiken
# Hafta 3 - Uzay Oyunu

import json
from pathlib import Path
from uzay_oyunu.araclar import hamle_sayaci
from uzay_oyunu.akis import yakit_gostergesi


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Mevcut envanter durumuna göre eşyaların listelendiği metni döndürür."""
    esyalar: list[str] = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("gelişmiş motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""
    return f"Sende: {', '.join(esyalar)}"


def hedef_menusu(hedefler: list[str]) -> str:
    """Verilen hedef listesinden numaralandırılmış seçim menüsü metni üretir."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)


def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs,
) -> dict:
    """Galaksi haritasını ve başlangıç durumunu kurar."""
    if baslangic not in gezegenler:
        raise ValueError(
            f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde bulunamadı!"
        )

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }


def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Depoya yakıt miktarı ekler."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def travel():
    """Oyuncunun galakside seyahat etmesini ve görevleri tamamlamasını sağlar."""
    json_yolu = Path(__file__).parent / "galaksi.json"
    with open(json_yolu, "r", encoding="utf-8") as f:
        veri = json.load(f)

    galaksi = galaksi_kur(**veri)
    sayac = hamle_sayaci()

    # Görev 2: Başlangıç yakıtı ve adım başı 5 birim tüketim
    gosterge = yakit_gostergesi(galaksi["yakit"], 5)

    credits = False
    engines = False
    copilot = False
    konum = galaksi["konum"]

    print("Uzay macerası başlıyor!")
    metin = envanter_metni(credits, engines, copilot)
    if metin:
        print(metin)

    destinations = galaksi["baglantilar"].get(konum, [])
    print(hedef_menusu(destinations))

    # Seyahat adımı simülasyonu ve yakıt kontrolü
    try:
        kalan = next(gosterge)
        hamle = sayac()
        print(f"Kalan yakıt: {kalan}")
        print(f"Oyunu {hamle} hamlede bitirdin!")
    except StopIteration:
        print("Yakıtın bitti, uzayda sürükleniyorsun...")


if __name__ == "__main__":
    travel()