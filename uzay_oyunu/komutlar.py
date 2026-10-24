# Ad Soyad: Berke Bağdiken
# Hafta 5 - Görev 4: Komut Sistemi ve Kayıt Deseni

from typing import Callable

KOMUTLAR: dict[str, tuple[Callable[[dict], str], str]] = {}


def komut(ad: str, aciklama: str = ""):
    """Fonksiyonu değiştirmeden KOMUTLAR sözlüğüne (fonksiyon, aciklama) olarak kaydeden dekoratör.

    Aynı komut adı iki kez tanımlanırsa ValueError fırlatır.
    """
    if ad in KOMUTLAR:
        raise ValueError(f"'{ad}' komutu zaten kayıtlı!")

    def dekorator(fonksiyon: Callable[[dict], str]) -> Callable[[dict], str]:
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayıtlı!")
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon

    return dekorator


@komut("yardim", "komutları listeler")
def yardim(durum: dict) -> str:
    """Mevcut komutları ve açıklamalarını alfabetik sırayla listeler."""
    satirlar = [f"{k} {v[1]}" for k, v in sorted(KOMUTLAR.items())]
    return "\n".join(satirlar)


@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum: dict) -> str:
    """Mevcut konumdan gidilebilecek bağlantılı gezegenleri virgülle listeler."""
    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {}).get(konum, [])
    return ", ".join(baglantilar)


@komut("envanter", "eşyalarını gösterir")
def envanter(durum: dict) -> str:
    """Oyuncunun envanterindeki eşyaları listeler."""
    esyalar: list[str] = []
    if durum.get("credits"):
        esyalar.append("bol kredi")
    if durum.get("engines"):
        esyalar.append("gelişmiş motorlar")
    if durum.get("copilot"):
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return "Envanter boş."
    return f"Sende: {', '.join(esyalar)}"