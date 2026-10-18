
## Hafta 4 - Görev 4: Önbellekli Rota Sayacı Performans Ölçümü
Gezegen: "dünya", Adım $n=20$ için `time.perf_counter()` ile yapılan karşılaştırma:
* **Önbelleksiz Süre:** 0.6575 saniye (Tekrarlı dallanmalar nedeniyle üstel zaman karmaşıklığı yaratır)
* **Önbellekli (@lru_cache) Süre:** 0.00003887 saniye (Dinamik programlama ve önbellek ile anında döner)
* **Hızlanma Oranı:** Yaklaşık 16.900 kat hızlanma
* **cache_info() Çıktısı:** `CacheInfo(hits=47, misses=51, maxsize=None, currsize=51)`
