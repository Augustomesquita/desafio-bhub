class PaymentProcessor:
    def process_payment(self, payment, payment_rule):
        print(payment)
        payment_rule.process_payment(payment)
        print("Fim do processo de pagamento.")
        print()
