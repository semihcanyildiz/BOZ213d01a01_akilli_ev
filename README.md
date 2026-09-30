# Akıllı Arşiv Odası Işık Simülasyonu 💡

Bu proje, Nesne Tabanlı Programlama (OOP) dersi kapsamında hazırlanmış bir akıllı otomasyon simülasyonudur. Bir iş yerindeki arşiv odası lambasının, mesai saatlerine göre otomatik olarak açılıp kapanmasını kontrol eden temel bir algoritmayı içerir.

## 🎯 Projenin Amacı
Mesai saatleri (08:00 - 17:00) içerisinde ışığın açık kalmasını, mesai dışında ise enerji tasarrufu sağlamak amacıyla otomatik kapanmasını sağlamak. Kullanıcıdan dinamik olarak saat verisi alınarak sistemin tepkisi anlık olarak test edilebilmektedir.

## ⚙️ Kullanılan OOP (Nesne Tabanlı Programlama) Kavramları
* **Sınıf (Class):** `ArsivIsigi` adında temel bir şablon oluşturulmuştur.
* **Nesne (Object):** Bu şablondan `arsiv` adında somut bir lamba nesnesi türetilmiştir.
* **Yapıcı Metot (__init__):** Işığın başlangıç durumu (kapalı) ve bulunduğu odanın adı (Arşiv Odası) tanımlanmıştır.
* **Metotlar (Methods):** Nesnenin yapabildiği eylemleri (durum bildirme, zamana göre karar verme) yöneten fonksiyonlar yazılmıştır.
* **Hata Yönetimi (Try-Except):** Kullanıcının saat yerine yanlışlıkla harf girmesi ihtimaline karşı programın çökmesini engelleyen güvenlik bloğu eklenmiştir.

## 🚀 Nasıl Çalıştırılır?
1. Proje dosyasını bilgisayarınıza indirin.
2. Python IDLE üzerinden açıp `F5` tuşuna basarak veya Terminal (CMD) ekranında dosya dizinine gidip aşağıdaki komutu yazarak simülasyonu başlatabilirsiniz:
   ```bash
   python akilli_ev.py
