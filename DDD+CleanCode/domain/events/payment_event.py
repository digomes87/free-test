from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PaymentCompleted:
    amount: Decimal
    final_amount: Decimal
    method: str
