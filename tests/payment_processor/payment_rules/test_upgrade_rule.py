import unittest
from unittest.mock import patch

from app.notifications.payment_notification import PaymentNotification
from app.payment_processor.payment_rules.upgrade_rule import UpgradeRule


class TestUpgradeRule(unittest.TestCase):
    def setUp(self):
        self.payment_notification = PaymentNotification()

    def test_upgrade_rule(self):
        with patch('builtins.print') as mock_print:
            upgrade_rule = UpgradeRule(self.payment_notification)
            upgrade_rule.process_payment('algum pagamento')
            mock_print.assert_called_with('Upgrade aplicado com sucesso!')


if __name__ == '__main__':
    unittest.main()
