from app.payment_processor.payment_processor import PaymentProcessor


class BookRule(PaymentProcessor):

    def process_payment(self, payment):
        print("Gerando guia de remessa duplicada para o departamento de royalties...")
        print("Guia de remessa duplicada para o departamento de royalties gerada com sucesso!")
        print("Pagamento de comissão para agente gerado com sucesso!")
