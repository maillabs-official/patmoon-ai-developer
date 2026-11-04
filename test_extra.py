import unittest
from researcher import trends,proposal
from telegram_control import handle_command
class ExtraTests(unittest.TestCase):
    def test_researcher(self):
        self.assertEqual(trends(lambda url:{"coins":[{"item":{"name":"Example","symbol":"EX"}}]})[0]["symbol"],"EX")
    def test_fallback(self): self.assertEqual(proposal([])["symbol"],"PATORB")
    def test_commands(self):
        on,msg=handle_command("/off")
        self.assertFalse(on)
        on,msg=handle_command("/simulasi",on)
        self.assertIn("OFF",msg)
        on,msg=handle_command("/on",on)
        self.assertTrue(on)
        on,msg=handle_command("/simulasi",on)
        self.assertIn("0 SOL virtual",msg)
    def test_help(self): self.assertIn("/on",handle_command("/help")[1])
if __name__=="__main__": unittest.main()
