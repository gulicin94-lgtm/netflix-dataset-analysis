"""
Gün 1 yardımcı komutları.
"""
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data"
CSV_FILE = DATA_PATH / "netflix_titles.csv"

def check_data():
    if CSV_FILE.exists():
        print(f"Veri bulundu: {CSV_FILE}")
    else:
        print("Uyarı: data/netflix_titles.csv bulunamadı. Kaggle'dan indirip bu klasöre koyun.")

if __name__ == "__main__":
    check_data()
