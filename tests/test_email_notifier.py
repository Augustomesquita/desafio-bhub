import unittest
from unittest.mock import patch

from notifiers.email_notifier import EmailNotifier


class TestEmailNotifier(unittest.TestCase):
    def test_update(self):
        with patch('builtins.print') as mock_print:
            email_notifier = EmailNotifier("test@example.com")
            email_notifier.update("Test message")
            mock_print.assert_called_with("E-mail enviado com sucesso.")


if __name__ == '__main__':
    unittest.main()
