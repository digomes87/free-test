from domain.services.strategies import CreditCardPayment, BoletoPayment, PixPayment
from application.use_cases.process_payment import PaymentProcessor


class Container:
    def __init__(self):
        self._services = {}

    def register(self, key, builder):
        self._services[key] = builder

    def resolve(self, key):
        builder = self._services.get(key)
        if builder is None:
            raise ValueError(f"Servico {key} não registrado")
        return builder()


container = Container()

container.register("credit_card", lambda: PaymentProcessor(CreditCardPayment()))
container.register("Boleto", lambda: PaymentProcessor(BoletoPayment()))
container.register("Pix", lambda: PaymentProcessor(PixPayment()))
