import pytest
from decimal import Decimal
from application.use_cases.process_payment import PaymentProcessor
from domain.services.strategies import CreditCardPayment, BoletoPayment, PixPayment


def test_credit_card_payment():
    processor = PaymentProcessor(CreditCardPayment())
    result = processor.execute(Decimal("100"))
    assert result == Decimal("105.00")


def test_invalid_amount():
    processor = PaymentProcessor(PixPayment())
    with pytest.raises(ValueError):
        processor.execute(Decimal("-1"))
