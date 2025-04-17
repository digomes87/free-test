from domain.entities.payments import PaymentMethod
from decimal import Decimal
from uuid import uuid4


class PaymentRecord:
    def __init__(self, id, method, amount, final_amount):
        self.id = id
        self.method = method
        self.amount = amount
        self.final_amount = final_amount


class InMemoryPaymentRepository:
    def __init__(self):
        self._store = []

    def save(self, method: str, amount: Decimal, final_amount: Decimal):
        record = PaymentRecord(str(uuid4()), method, amount, final_amount)
        self._store.append(record)
        return record

    def list_all():
        return self._store
