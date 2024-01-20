class PaymentNotification:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
