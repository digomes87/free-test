from decimal import Decimal
from domain.entities.payments import PaymentMethod


class CreditCardPayment(PaymentMethod):
    def process(self, amount: Decimal) -> Decimal:
        return amount * Decimal("1.05")


class BoletoPayment(PaymentMethod):
    def process(self, amount: Decimal) -> Decimal:
        return amount * Decimal("1.015")


class PixPayment(PaymentMethod):
    def process(self, amount: Decimal) -> Decimal:
        return amount


        
