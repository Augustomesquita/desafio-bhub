import unittest
from unittest.mock import patch

from app.payment_processor.payment_rules.book_rule import BookRule


class TestBookRule(unittest.TestCase):
    def test_book_rule(self):
        with patch('builtins.print') as mock_print:
            book_rule = BookRule()
            book_rule.process_payment('algum pagamento')
            mock_print.assert_called_with('Pagamento de comissão para agente gerado com sucesso!')


if __name__ == '__main__':
    unittest.main()
