"""Optional Telegram report for the OFFCHAIN simulation. Secrets via environment only."""
import json
import os
import sys
import urllib.parse
import urllib.request
from simulator import simulate

def format_report(data):
    lines = [
        "🧪 PATMOON | SIMULASI SAJA",
        "REAL OFF • Tidak ada SOL sungguhan",
        "👛 3 wallet virtual masing-masing membeli 1 SOL virtual",
        "💧 Pool sebelum penarikan: 8 SOL virtual",
        "📤 LP virtual ditarik: 100%",
        "💧 Pool sesudah: 0 SOL virtual",
        "⚠️ Token pembeli tetap di wallet, tetapi pool kosong.",
        "Tidak ada transaksi blockchain."
    ]
    return "\n".join(lines)

def main():
    result = simulate()
    message = format_report(result)
    print(message)
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not token or not chat:
        print("Telegram belum dikonfigurasi; laporan hanya ditampilkan di log.")
        return 0
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({"chat_id": chat, "text": message}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=payload), timeout=15) as resp:
            data = json.load(resp)
            if not data.get("ok"):
                raise RuntimeError("Telegram rejected report")
        print("Telegram menerima laporan simulasi.")
        return 0
    except Exception as exc:
        print(f"Gagal mengirim laporan Telegram: {type(exc).__name__}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
