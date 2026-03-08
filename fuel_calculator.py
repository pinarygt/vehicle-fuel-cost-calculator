def hesapla():
    print("-" * 30)
    print("  ARAÇ YAKIT HESAPLAYICI  ")
    print("-" * 30)
    
    try:
        mesafe = float(input("Gidilecek mesafe (km): "))
        tuketim = float(input("Ortalama tüketim (L/100km): "))
        fiyat = float(input("Yakıtın litre fiyatı (TL): "))

        toplam_litre = (mesafe / 100) * tuketim
        toplam_maliyet = toplam_litre * fiyat

        print("-" * 30)
        print(f"Toplam tüketilen yakıt: {toplam_litre:.2f} Litre")
        print(f"Toplam maliyet: {toplam_maliyet:.2f} TL")
        print("-" * 30)
        
        input("Çıkmak için Enter'a basın...") # Ekranın hemen kapanmaması için
    except ValueError:
        print("Hata: Lütfen sadece sayı giriniz!")

if __name__ == "__main__":
    hesapla()