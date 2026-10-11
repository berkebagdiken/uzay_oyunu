# Ad Soyad: Berke Bağdiken
# Hafta 3 - Uzay Oyunu

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


def travel():
    """Oyuncunun galakside seyahat etmesini ve görevleri tamamlamasını sağlar."""
    credits = False
    engines = False
    copilot = False
    konum = "dünya"

    destinations_map = {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "kara_delik": ["sirius"]
    }

    print("Uzay macerası başlıyor!")
    metin = envanter_metni(credits, engines, copilot)
    if metin:
        print(metin)

    destinations = destinations_map.get(konum, [])
    print(hedef_menusu(destinations))


if __name__ == "__main__":
    travel()