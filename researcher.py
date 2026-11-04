"""Read-only public trending feed; not an AI model or trading bot."""
import json
import urllib.request
URL = "https://api.coingecko.com/api/v3/search/trending"
def trends(fetch=None):
    if fetch is None:
        def fetch(url):
            req = urllib.request.Request(url, headers={"User-Agent":"PATMOON-Research-Demo/1.0","Accept":"application/json"})
            with urllib.request.urlopen(req,timeout=12) as resp: return json.load(resp)
    data=fetch(URL)
    out=[]
    for entry in data.get("coins",[])[:8]:
        item=entry.get("item") or {}
        name=str(item.get("name") or "").strip()[:80]
        symbol=str(item.get("symbol") or "").strip()[:20]
        if name and symbol: out.append({"name":name,"symbol":symbol})
    return out
def proposal(items):
    if not items:
        return {"name":"PATMOON Orbit","symbol":"PATORB","tagline":"Meme penjelajah bulan","basis":"Contoh lokal; data tren tidak tersedia"}
    seed=items[0]
    return {"name":"PATMOON Orbit","symbol":"PATORB","tagline":"Maskot astronaut kucing emas menjelajah meme galaxy","basis":f"Referensi tren umum: {seed['name']} ({seed['symbol']}); tidak meniru identitas token"}
