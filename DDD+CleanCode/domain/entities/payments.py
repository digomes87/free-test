from abc import ABC, abstractmethod
from decimal import Decimal


class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount: Decimal) -> Decimal:
        pass

    
