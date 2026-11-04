"""Create read-only trend and virtual-token concept report."""
import json
from researcher import trends,proposal
from telegram_report import format_report
from simulator import simulate
def main():
    try:
        items=trends()
        status="Sumber publik berhasil dibaca."
    except Exception:
        items=[]
        status="Data tren publik tidak tersedia; konsep contoh, bukan tren terbaru."
    p=proposal(items)
    print("📊 PATMOON RESEARCH (REAL OFF)")
    print(status)
    for item in items[:5]:
        print(f"- {item['name']} ({item['symbol']})")
    print(f"Konsep: {p['name']} ({p['symbol']})")
    print(f"Deskripsi: {p['tagline']}")
    print(f"Dasar: {p['basis']}")
    print("Tidak membuat token asli dan tidak merekomendasikan pembelian.")
if __name__=="__main__": main()
