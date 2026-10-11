# Ad Soyad: Berke Bağdiken
# Hafta 3 - Uzay Oyunu

import json
from pathlib import Path


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Mevcut envanter durumuna göre eşyaların listelendiği metni döndürür.
    
    Hiçbir eşya yoksa boş dize döndürür.
    """
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
    """Galaksi haritasını ve başlangıç durumunu kurar.
    
    Başlangıç gezegeni listede yoksa ValueError fırlatır.
    Yakit belirtilmezse varsayılan 50 olarak atanır.
    """
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde bulunamadı!")

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }


def travel():
    """Oyuncunun galakside seyahat etmesini ve görevleri tamamlamasını sağlar."""
    # JSON dosyasını okuyup galaksiyi kurma
    json_yolu = Path(__file__).parent / "galaksi.json"
    with open(json_yolu, "r", encoding="utf-8") as f:
        veri = json.load(f)

    galaksi = galaksi_kur(**veri)

    credits = False
    engines = False
    copilot = False
    konum = galaksi["konum"]

    print("Uzay macerası başlıyor!")
    metin = envanter_metni(credits, engines, copilot)
    if metin:
        print(metin)

    # Hedefleri doğrudan galaksi sözlüğünden alma
    destinations = galaksi["baglantilar"].get(konum, [])
    print(hedef_menusu(destinations))


if __name__ == "__main__":
    travel()