import unittest
from unittest.mock import patch

from app.notifications.payment_notification import PaymentNotification


class TestPaymentNotification(unittest.TestCase):
    def setUp(self):
        self.payment_notification = PaymentNotification()

    def test_register_observer(self):
        observer_mock = unittest.mock.Mock()
        self.payment_notification.register_observer(observer_mock)
        self.assertIn(observer_mock, self.payment_notification.observers)

    def test_unregister_observer(self):
        observer_mock = unittest.mock.Mock()
        self.payment_notification.observers = [observer_mock]
        self.payment_notification.unregister_observer(observer_mock)
        self.assertNotIn(observer_mock, self.payment_notification.observers)

    def test_notify(self):
        observer_mock = unittest.mock.Mock()
        self.payment_notification.observers = [observer_mock]
        self.payment_notification.notify("Test message")
        observer_mock.update.assert_called_once_with("Test message")


if __name__ == '__main__':
    unittest.main()
