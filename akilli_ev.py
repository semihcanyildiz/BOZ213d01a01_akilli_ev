# Arşiv odası ışık kontrolü için yeni sınıfımız
class ArsivIsigi:
    
    def __init__(self, oda_adi):
        self.oda_adi = oda_adi
        self.isik_acik = False  # Güvenlik için başlangıçta ışığı kapalı kabul ediyoruz

    def durum_bildir(self):
        # Işık durumuna göre ekrana Açık veya Kapalı yazdırır
        durum = "AÇIK" if self.isik_acik else "KAPALI"
        print(f"[{self.oda_adi}] Güncel Durum: Işıklar {durum}")

    def saati_guncelle(self, saat):
        print(f"\n--- Sistem Saati: {saat:02d}:00 ---") 
        
        # MESAİ SAATLERİ: Saat 8 ile 17 (hariç) arası. Yani 08:00 - 16:59 arası.
        if 8 <= saat < 17:
            # Eğer saat aralığı uyuyorsa ve ışık kapalıysa, ışığı aç.
            if not self.isik_acik: 
                self.isik_acik = True
                print("Mesai başladı! Arşiv odası ışıkları AÇILDI.")
            else:
                # Işık zaten açıksa gereksiz işlem yapma, sadece bilgi ver.
                print("Mesai devam ediyor. Işıklar zaten AÇIK.")
                
        # MESAİ DIŞI SAATLER: Saat 17'den büyük veya 8'den küçükse
        else:
            # Mesai bitmiş ve ışık hala açıksa, ışığı kapat.
            if self.isik_acik:
                self.isik_acik = False
                print("Mesai bitti! Enerji tasarrufu için ışıklar KAPATILDI.")
            else:
                # Işık zaten kapalıysa sadece bilgi ver.
                print("Mesai dışındayız. Işıklar zaten KAPALI.")

# ================= ANA PROGRAM =================

arsiv = ArsivIsigi("Arşiv Odası")

print("--- AKILLI İŞ YERİ SİSTEMİ BAŞLATILDI ---")
arsiv.durum_bildir()

# Kullanıcıdan sürekli saat isteme döngüsü
while True:
    giris = input("\nLütfen güncel saati girin (0-24) veya çıkmak için 'q' tuşuna basın: ")
    
    if giris.lower() == 'q':
        print("Sistem kapatılıyor. İyi çalışmalar!")
        break
        
    try:
        saat_degeri = int(giris)
        
        if 0 <= saat_degeri <= 24:
            arsiv.saati_guncelle(saat_degeri)
        else:
            print("Hata: Lütfen 0 ile 24 arasında geçerli bir saat giriniz.")
            
    except ValueError:
        print("Hata: Lütfen sadece rakam giriniz!")
