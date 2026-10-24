# Dekoratör Sırası ve Çağrı Sayısı Analizi

Özyinelemeli Fibonacci fonksiyonu `fib(20)` için farklı dekoratör dizilimlerinin çağrı sayıları:

| Durum | Dekoratör Sırası | `fib(20)` Çağrı Sayısı |
| :--- | :--- | :--- |
| **1. Durum** | Yalnızca `@say` | **21891** |
| **2. Durum** | `@say` üstte, `@lru_cache` altta | **39** |
| **3. Durum** | `@lru_cache` üstte, `@say` altta | **21** |

---

## Sonuçların Neden Farklı Olduğunun Açıklaması

Python'da dekoratörler fonksiyon tanımına en yakın olandan başlayarak **aşağıdan yukarıya** doğru uygulanır (zincirlenir).

### 1. Yalnızca `@say` (21891 Çağrı)
* Önbellekleme (memoization) bulunmaz.
* Ağaç yapısındaki her alt dal (örneğin `fib(3)`, `fib(4)`) bağımsız olarak tekrar tekrar hesaplanır.
* Üstel zaman karmaşıklığı ($O(2^n)$) nedeniyle fonksiyon gövdesi tam **21891** kez tetiklenir ve sayaç her çağrıda bir artar.

### 2. `@say` Üstte, `@lru_cache` Altta (39 Çağrı)
* Sözdizimi: `say(lru_cache(fib))`.
* En dıştaki katman `@say` sarmalayıcısıdır.
* İçerideki özyinelemeli çağrılar (`fib(n-1) + fib(n-2)`) doğrudan en dıştaki `fib` fonksiyonunu çağırdığı için, istek **önbellekten dönse bile (cache hit)** önce `@say` sarmalayıcısından geçer.
* Toplam 21 önbellek ıskalaması (cache miss) + 18 önbellek isabeti (cache hit) gerçekleşir; sayaç her ikisini de sayarak **39** değerine ulaşır.

### 3. `@lru_cache` Üstte, `@say` Altta (21 Çağrı)
* Sözdizimi: `lru_cache(say(fib))`.
* En dıştaki katman `@lru_cache` dekoratörüdür.
* Fonksiyon çağrıldığında istek ilk olarak `@lru_cache` katmanına ulaşır. Sonuç önbellekte mevcutsa, alttaki fonksiyona hiç inilmeden doğrudan döndürülür.
* Alttaki `@say` dekoratörü yalnızca önbellekte değer bulunmadığında (cache miss) çalışır.
* $n = 0, 1, 2, \dots, 20$ olmak üzere toplam **21** benzersiz girdi olduğu için sayaç tam **21** kez çalışır.
* Dış katmanda `@lru_cache` bulunduğu için içteki sayaca `fib.__wrapped__.cagri` üzerinden erişilir.
