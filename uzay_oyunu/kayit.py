# Ad Soyad: Berke Bağdiken
# Hafta 3 - Görev 2: Esnek Parametreler


def gorev_kaydi(
    baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str
) -> str:
    """Görev başlığını, adımlarını ve ek bilgileri biçimlendirilmiş bir metin olarak döndürür."""
    satirlar = [f"[{oncelik.upper()}] {baslik}"]

    for i, adim in enumerate(adimlar, start=1):
        satirlar.append(f"{i}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f"{anahtar}: {deger}")

    return "\n".join(satirlar)


if __name__ == "__main__":
    # 1. Doğrudan argümanlarla çağırma
    cikti1 = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Berke",
    )
    print("--- 1. Doğrudan Çağrı ---")
    print(cikti1)

    # 2. Liste (*) ve sözlük (**) açarak (unpacking) çağırma
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Berke"}

    cikti2 = gorev_kaydi(
        "Kara deliğe atla",
        *adimlar,
        oncelik="yüksek",
        **ekler,
    )
    print("\n--- 2. Liste (*) ve Sözlük (**) Açarak Çağrı ---")
    print(cikti2)