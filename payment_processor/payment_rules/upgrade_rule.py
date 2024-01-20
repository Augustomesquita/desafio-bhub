from notifications.payment_notification import PaymentNotification
from payment_processor.payment_processor import PaymentProcessor


class UpgradeRule(PaymentProcessor):

    def __init__(self, payment_notifier: PaymentNotification):
        self.payment_notifier = payment_notifier

    def process_payment(self, payment):
        print("Aplicando upgrade...")
        print("Upgrade aplicado com sucesso!")
        self.payment_notifier.notify(f'Recebemos seu pagamento e a aplicação de upgrade foi realizada com sucesso.')
