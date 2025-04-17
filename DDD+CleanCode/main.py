from decimal import Decimal
from application.use_cases.process_payment import PaymentProcessor
from domain.services.strategies import PixPayment, CreditCardPayment, BoletoPayment
from infra.gateways.logger import log_payment


if __name__ == "__main__":
    amount = Decimal("200")
    payment = PaymentProcessor(CreditCardPayment())
    final = payment.execute(amount)
    log_payment("Cartão", float(amount), float(final))
