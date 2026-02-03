# Netflix İçerik Analizi — Proje İskeleti (Gün 1)

Bu klasör **Gün 1: Kurulum & Veri Hazırlığı** için hazırlandı.

## Yapılacaklar (Checklist)
- [ ] Python ortamını kur (aşağıdaki `requirements.txt` ile)
- [ ] Kaggle'dan `netflix_titles.csv` indir ve `data/` klasörüne koy
- [ ] `notebooks/01_setup_and_load.ipynb` notebook'unu aç, ilk hücreleri çalıştır
- [ ] Veri ön incelemesi: `head()`, `info()`, `describe()`

## Kısayol Komutlar
```bash
# (Öneri) Sanal ortam
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Gerekli paketler
pip install -r requirements.txt

# Jupyter başlat
jupyter notebook
# veya
jupyter lab
```

## Veri Seti
- Kaggle: **Netflix Movies and TV Shows Dataset** (yapımcı: shivamb)
- Dosya adı: `netflix_titles.csv`
- Bu dosyayı indirip `data/` klasörüne yerleştir.

> Not: Kaggle hesabın yoksa ücretsiz açabilirsin. İndirdikten sonra bu klasöre `netflix_titles.csv` olarak kopyala.

## Sonraki Adımlar
Gün 2'de veri yükleme ve hızlı inceleme (EDA'ya hazırlık) yapılacak.
