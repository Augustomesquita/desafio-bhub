import unittest
from unittest.mock import patch

from app.payment_processor.payment_rules.physical_product_rule import PhysicalProductRule


class TestPhysicalProductRule(unittest.TestCase):
    def test_physical_product_rule(self):
        with patch('builtins.print') as mock_print:
            physical_product_rule = PhysicalProductRule()
            physical_product_rule.process_payment('algum pagamento')
            mock_print.assert_called_with('Pagamento de comissão para agente gerado com sucesso!')


if __name__ == '__main__':
    unittest.main()
