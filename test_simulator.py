import unittest
from simulator import simulate
from telegram_report import format_report

class TestSimulation(unittest.TestCase):
    def test_safe_mode(self):
        r = simulate()
        self.assertEqual(r["mode"], "OFFCHAIN_SIMULATION_REAL_OFF")
        self.assertEqual(r["pool_after_lp_removal"]["virtual_sol"], 0)
        self.assertEqual(len(r["buyer_wallets"]), 3)
        self.assertEqual(r["developer_virtual_assets_removed"]["virtual_sol"], 8)
        self.assertFalse(r["buyers_can_sell_in_removed_pool"])
        self.assertTrue(all(w["tokens_held"] > 0 for w in r["buyer_wallets"].values()))

    def test_report(self):
        message = format_report(simulate())
        self.assertIn("SIMULASI", message)
        self.assertIn("REAL OFF", message)

if __name__ == "__main__":
    unittest.main()
