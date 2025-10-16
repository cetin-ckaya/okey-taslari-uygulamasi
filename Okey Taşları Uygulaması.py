import random

# a) Tüm okey taşlarını oluştur (4 renk, 1-13 arası sayılar, her taştan 2 tane)
renkler = ["turuncu", "kırmızı", "mavi", "siyah"]
okey_taslari = [(renk, sayi) for renk in renkler for sayi in range(1, 14)] * 2  # 104 taş

# b) Generator fonksiyonu
def tasCek(taslar):
    while taslar:
        secilen = random.choice(taslar)
        taslar.remove(secilen)
        yield secilen
    yield "Yerde taş kalmadı."

# c) 104 taş bitene kadar çekip ekrana yazdır
for tas in tasCek(okey_taslari):
    if tas == "Yerde taş kalmadı.":
        print("\n", tas)
    else:
        print(f"{tas}", end=" | ")
