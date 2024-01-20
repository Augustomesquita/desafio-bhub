class EmailNotifier:
    def __init__(self, email_address):
        self.email_address = email_address

    def update(self, message):
        self.send_email(message)

    def send_email(self, message):
        print("Preparando para enviar e-mail de notificação...")
        print(f"Enviando e-mail para '{self.email_address}' com a seguinte mensagem: {message}")
        print("E-mail enviado com sucesso.")

