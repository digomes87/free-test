from decimal import Decimal
from domain.entities.payments import PaymentMethod


class PaymentProcessor:
    def __init__(self, strategy: PaymentMethod):
        self.strategy = strategy

    def execute(self, amount: Decimal) -> Decimal:
        self._validate(amount)
        return self.strategy.process((amount))

    def _validate(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("O valor deve ser positivo")
