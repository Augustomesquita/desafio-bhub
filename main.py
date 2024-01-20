from notifications.payment_notification import PaymentNotification
from notifiers.email_notifier import EmailNotifier
from payment_processor.payment_processor import PaymentProcessor
from payment_processor.payment_rules.book_rule import BookRule
from payment_processor.payment_rules.upgrade_rule import UpgradeRule
from payment_processor.payment_rules.physical_product_rule import PhysicalProductRule

if __name__ == "__main__":
    # Cria instâncias para notificação
    payment_notification = PaymentNotification()

    # Instancia e registra notificador(es)
    email_notifier = EmailNotifier("cliente_bhub@example.com")
    payment_notification.register_observer(email_notifier)

    # Cria instâncias das estratégias
    physical_product_rule = PhysicalProductRule()
    book_rule = BookRule()

    # Cria instância de estratégia que utiliza notificacao
    upgrade_rule = UpgradeRule(payment_notification)

    # Cria instância do processador de pagamentos
    payment_processor = PaymentProcessor()

    # Processar pagamentos usando diferentes estratégias
    payment_processor.process_payment("Pagamento para produto físico", physical_product_rule)
    payment_processor.process_payment("Pagamento para livro", book_rule)
    payment_processor.process_payment("Pagamento para aplicação de upgrade", upgrade_rule)
