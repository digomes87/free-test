from fastapi import APIRouter, HTTPException
from decimal import Decimal

from api.schemas import PaymentRequest, PaymentResponse
from infra.container import container
from infra.repositories.in_memory import InMemoryPaymentRepository
from domain.events.payment_event import PaymentCompleted
from infra.event_bus import publish


router = APIRouter()


@router.post("/pagamentos", response_model=PaymentResponse)
def processar_pagamento(request: PaymentRequest):
    try:
        processor = container.resolve(request.method)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    amount = Decimal(str(request.amount))
    result = processor.execute(amount)

    repo = InMemoryPaymentRepository()
    repo.save(request.method, amount, result)

    event = PaymentCompleted(amount=amount, final_amount=result, method=request.method)
    publish(event)

    return PaymentResponse(
        original_amount=float(amount),
        final_amount=float(result),
        method=request.method
    )
