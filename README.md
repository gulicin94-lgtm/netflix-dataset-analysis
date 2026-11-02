# Netflix İçerik Analizi

Netflix içerik kataloğu üzerinde Python ile yapılan keşifsel veri analizi (EDA) ve temel metin analizi (NLP) çalışması.

## Amaç

Netflix'teki film ve dizi içeriklerinin dağılımını incelemek, içerik türleri arasındaki farkları görselleştirmek ve içerik açıklamalarında öne çıkan anahtar kelimeleri belirlemek.

## Veri Seti

- Kaynak: Kaggle, **Netflix Movies and TV Shows** (yapımcı: shivamb)
- Dosya: `netflix_titles.csv` (`data/` klasörüne konur)
- Kayıt sayısı: **[KAYIT SAYISI]**

## Yöntem

1. **Veri hazırlığı:** Eksik ve tutarsız değerlerin tespiti ve temizlenmesi (**[ör. hangi sütunlarda eksik veri vardı, nasıl ele alındı]**)
2. **Keşifsel veri analizi:** Film ve dizi dağılımlarının karşılaştırmalı incelenmesi, içerik türü farklılıklarının görselleştirilmesi
3. **Metin analizi (NLP):** İçerik açıklamaları üzerinde temel ön işleme ve sık geçen anahtar kelimelerin belirlenmesi
4. **Raporlama:** Sonuçların grafik ve tablolarla özetlenmesi

## Temel Bulgular

- **[BULGU 1, ör. film / dizi oranı ve bunun yıllara göre değişimi]**
- **[BULGU 2, ör. en yaygın içerik türleri ya da ülkeler]**
- **[BULGU 3, ör. açıklamalarda en sık geçen anahtar kelimeler]**


## Kullanılan Araçlar

- Python
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook

## Proje Yapısı

```
netflix-dataset-analysis/
├── data/            # Ham veri (netflix_titles.csv)
├── notebooks/       # Analiz notebook'ları
├── src/             # Yardımcı kodlar
├── requirements.txt
└── README.md
```

## Çalıştırma

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Yazar

Güliçin Aktaş

## Sonraki Adımlar
Gün 2'de veri yükleme ve hızlı inceleme (EDA'ya hazırlık) yapılacak.
