# Kapsam (Scope) ve İsim Alanı Analizi
**Öğrenci:** Berke Bağdiken

---

## Örnek 1: Global Değişkeni Fonksiyon İçinden Okuma
```python
x = 10
def oku():
    print("Değer:", x)
oku()
x = 10
def degistir():
    x = 20
    print("Yerel:", x)
degistir()
print("Global:", x)
x = 15
def print_x():
    print("x'in değeri:", x)
    x = 20  # Yerel atama
print_x()
def yakit_ekle(miktar, depo=[]):
    depo.append(miktar)
    return depo