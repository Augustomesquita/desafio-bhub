import unittest
from unittest.mock import patch

from app.notifications.payment_notification import PaymentNotification
from app.payment_processor.payment_processor import PaymentProcessor
from app.payment_processor.payment_rules.book_rule import BookRule
from app.payment_processor.payment_rules.physical_product_rule import PhysicalProductRule
from app.payment_processor.payment_rules.upgrade_rule import UpgradeRule


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.payment_notification = PaymentNotification()
        self.payment_processor = PaymentProcessor()

    def test_process_physical_product_payment(self):
        with patch('builtins.print') as mock_print:
            physical_product_rule = PhysicalProductRule()
            self.payment_processor.process_payment("Pagamento para produto físico", physical_product_rule)
            mock_print.assert_called_with()

    def test_process_book_payment(self):
        with patch('builtins.print') as mock_print:
            book_rule = BookRule()
            self.payment_processor.process_payment("Pagamento para livro", book_rule)
            mock_print.assert_called_with()

    def test_process_upgrade_payment(self):
        with patch('builtins.print') as mock_print:
            payment_notification = PaymentNotification()
            with patch.object(payment_notification, 'notify') as mock_notify:
                upgrade_rule = UpgradeRule(payment_notification)
                upgrade_rule.process_payment("Pagamento para aplicação de upgrade")
                mock_print.assert_called_with("Upgrade aplicado com sucesso!")
                mock_notify.assert_called_with(
                    'Recebemos seu pagamento e a aplicação de upgrade foi realizada com sucesso.')


if __name__ == '__main__':
    unittest.main()
