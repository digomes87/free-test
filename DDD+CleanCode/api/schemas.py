from pydantic import BaseModel

class PaymentRequest(BaseModel):
    amount: float
    method: str


class PaymentResponse(BaseModel):
    original_amount: float
    final_amount: float
    mehtod: str
