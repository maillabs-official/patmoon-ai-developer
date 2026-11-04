"""Commands control only a virtual simulation."""
from simulator import simulate
from researcher import proposal
def handle_command(command,enabled=True,trends=None):
    cmd=(command or "").split()[0].lower().split("@")[0] if (command or "").split() else ""
    if cmd=="/off": return False,"🔴 PATMOON SIMULASI: OFF"
    if cmd=="/on": return True,"🟢 PATMOON SIMULASI: ON (REAL OFF)"
    if cmd in ("/start","/help"): return enabled,"Perintah: /on /off /simulasi /tren /help. Semua virtual; tidak ada trading."
    if not enabled: return enabled,"Simulator OFF. Ketik /on."
    if cmd=="/simulasi":
        r=simulate()
        return enabled,f"🧪 PATMOON: 3 wallet membeli 1 SOL virtual masing-masing. Pool sebelum LP ditarik: {r['pool_before_lp_removal']['virtual_sol']} SOL virtual. Setelah penarikan 100% LP: 0 SOL virtual. Pembeli tetap memegang token."
    if cmd=="/tren":
        p=proposal(trends or [])
        return enabled,f"📊 Konsep token (bukan token nyata): {p['name']} (${p['symbol']}). {p['tagline']}. {p['basis']}"
    return enabled,"Perintah tidak dikenal. Ketik /help."
