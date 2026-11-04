# PATMOON AI Developer — Educational Virtual Simulation

**REAL OFF.** No real SOL, Phantom, private keys, token minting, or Mainnet transactions. All buys and LP removal are illustrative.

## Included
- `simulator.py`: 3 virtual wallets buy into a constant-product pool; developer withdraws all simulated LP.
- `test_simulator.py`, `test_extra.py`: offline unit tests.
- `researcher.py`: read-only CoinGecko trending feed; errors fall back to an explicitly labelled sample.
- `daily_report.py`: trend and original token concept text, **not a generative AI model**.
- `telegram_control.py`: virtual-only commands `/on`, `/off`, `/simulasi`, `/tren`, `/help`.
- `bot.py`: Telegram long-polling bot for a **separately hosted persistent machine**; not running on GitHub Actions.
- `telegram_report.py`: optional manual-run Telegram simulation report.

## Run locally
```bash
python -m unittest discover -v
python simulator.py
python daily_report.py
```

To run the Telegram command bot, configure `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in your host's environment and run `python bot.py` on a persistent host. Do not commit secrets. Bot ON/OFF state is in-memory and resets to ON after restart; a persistent store is needed for durable state. Group/chat commands require appropriate Telegram permissions. Avoid running multiple getUpdates consumers for the same bot.

## GitHub Actions
Workflow `PATMOON Virtual Simulation` runs on push, manual dispatch, and a daily schedule at 23:00 UTC (08:00 WIT). It produces `report.json` and `trends.txt` artifacts. Telegram simulation message is sent only on manual dispatch **if** both repository secrets are configured.

**Not yet verified:** GitHub Actions successful run, Telegram live delivery, or persistent bot hosting. GitHub Actions is not an always-on Telegram command server.
