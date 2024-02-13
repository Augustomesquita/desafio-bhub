import unittest
from unittest.mock import patch

from app.notifications.payment_notification import PaymentNotification
from app.payment_processor.payment_processor import PaymentProcessor
from app.payment_processor.payment_rules.book_rule import BookRule
from app.payment_processor.payment_rules.physical_product_rule import PhysicalProductRule
from app.payment_processor.payment_rules.upgrade_rule import UpgradeRule


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.payment_processor = PaymentProcessor()

    @patch.object(PhysicalProductRule, 'process_payment')
    def test_process_physical_product_payment(self, mock_physical_product_rule_process_payment):
        physical_product_rule = PhysicalProductRule()
        self.payment_processor.process_payment("Pagamento para produto físico", physical_product_rule)
        mock_physical_product_rule_process_payment.assert_called_once()

    @patch.object(BookRule, 'process_payment')
    def test_process_book_payment(self, mock_book_rule_process_payment):
        book_rule = BookRule()
        self.payment_processor.process_payment("Pagamento para livro", book_rule)
        mock_book_rule_process_payment.assert_called_once()

    @patch.object(UpgradeRule, 'process_payment')
    def test_process_upgrade_payment(self, mock_upgrade_rule_process_payment):
        payment_notification = PaymentNotification()
        upgrade_rule = UpgradeRule(payment_notification)
        self.payment_processor.process_payment("Pagamento para aplicação de upgrade", upgrade_rule)
        mock_upgrade_rule_process_payment.assert_called_once()


if __name__ == '__main__':
    unittest.main()
