# FLO Customer Data Analysis

Bu proje, FLO markasının müşteri verilerini kullanarak yapılan **exploratory data analysis (EDA)** çalışmasını içermektedir. Python ile hazırlanmış olup temel veri analizi, kategorik ve sayısal değişken incelemesi, korelasyon analizi ve basit görselleştirmeleri kapsamaktadır.

## İçerik

- `serbest2.py`: Python script dosyası, tüm veri analizi kodlarını içerir.
- `flo_data_20k.csv`: Kullanılan FLO müşteri veri seti. Miuul'un Machine Learning dersinde öğrencilere aktardığı eski verilere dayanmaktadır.

## Yapılan Analizler

1. Dataset genel bilgileri (`head`, `info`, `describe`, `isnull` kontrolü)
2. Kategorik ve sayısal değişkenlerin ayrımı
3. Kategorik değişkenlerin dağılım analizi
4. Sayısal değişkenlerin özet istatistikleri ve quantile analizi
5. Korelasyon analizi ve ısı haritası
6. Basit feature engineering (toplam sipariş, toplam harcama)
7. Online vs offline harcama karşılaştırması
8. En değerli müşterilerin analizi
9. Ortalama sipariş değeri (AOV) hesaplama
10. Basit segmentasyon analizi

## Kullanım

1. Python ve gerekli kütüphaneler yüklü olmalıdır:
   ```bash
   pip install pandas numpy matplotlib seaborn
