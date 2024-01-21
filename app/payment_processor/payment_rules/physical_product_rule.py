from app.payment_processor.payment_processor import PaymentProcessor


class PhysicalProductRule(PaymentProcessor):
    def process_payment(self, payment):
        print("Gerando guia de remessa para envio...")
        print("Guia de remessa para envio gerada com sucesso!")
