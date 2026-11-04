"""PATMOON educational liquidity-withdrawal simulation. No blockchain, wallets or real money."""
from dataclasses import dataclass
import json

@dataclass
class Pool:
    sol: float = 5.0
    token: float = 1_000_000.0
    lp_owner: str = "Developer"

def simulate():
    pool = Pool()
    wallets = {}
    log = []
    for i in range(1, 4):
        spend = 1.0
        tokens_out = pool.token * spend / (pool.sol + spend)
        pool.sol += spend
        pool.token -= tokens_out
        wallets[f"W{i}"] = {"virtual_sol_spent": spend, "tokens_held": round(tokens_out, 4)}
        log.append({"event": "BUY_VIRTUAL", "wallet": f"W{i}", "sol": spend, "tokens": round(tokens_out, 4)})
    before = {"virtual_sol": round(pool.sol, 6), "tokens": round(pool.token, 4)}
    removed = before.copy()
    pool.sol = 0
    pool.token = 0
    log.append({"event": "REMOVE_ALL_LP_SIMULATED", "owner": "Developer", "virtual_sol": removed["virtual_sol"], "tokens": removed["tokens"]})
    return {
        "mode": "OFFCHAIN_SIMULATION_REAL_OFF",
        "token": "PATMOON",
        "starting_pool_virtual_sol": 5,
        "pool_before_lp_removal": before,
        "developer_virtual_assets_removed": removed,
        "pool_after_lp_removal": {"virtual_sol": pool.sol, "tokens": pool.token},
        "buyer_wallets": wallets,
        "buyers_can_sell_in_removed_pool": False,
        "note": "Buyer wallet token balances remain unchanged; this simulates LP withdrawal, not wallet theft. Assumes developer owns 100% LP. No blockchain transaction.",
        "events": log
    }

if __name__ == "__main__":
    print(json.dumps(simulate(), ensure_ascii=False, indent=2))
