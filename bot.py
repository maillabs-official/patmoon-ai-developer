"""Persistent Telegram polling bot; virtual only. Requires separate always-on hosting."""
import json,os,time,urllib.parse,urllib.request
from researcher import trends
from telegram_control import handle_command
TOKEN=os.environ.get("TELEGRAM_BOT_TOKEN","")
CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID","")
def api(method,params):
    url=f"https://api.telegram.org/bot{TOKEN}/{method}"
    with urllib.request.urlopen(urllib.request.Request(url,data=urllib.parse.urlencode(params).encode()),timeout=35) as resp:
        result=json.load(resp)
    if not result.get("ok"): raise RuntimeError("Telegram API rejected request")
    return result["result"]
def run():
    if not TOKEN or not CHAT_ID: raise SystemExit("Configure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID")
    offset=None
    enabled=True
    while True:
        try:
            updates=api("getUpdates",{"timeout":20,**({"offset":offset} if offset is not None else {})})
            for update in updates:
                offset=update["update_id"]+1
                message=update.get("message") or update.get("channel_post") or {}
                if str((message.get("chat") or {}).get("id"))!=CHAT_ID: continue
                command=message.get("text","")
                try: items=trends() if command.split(" ")[0].lower()=="/tren" and enabled else []
                except Exception: items=[]
                enabled,response=handle_command(command,enabled,items)
                api("sendMessage",{"chat_id":CHAT_ID,"text":response})
        except KeyboardInterrupt: break
        except Exception as exc:
            print(f"Retry after {type(exc).__name__}",flush=True)
            time.sleep(5)
if __name__=="__main__": run()
