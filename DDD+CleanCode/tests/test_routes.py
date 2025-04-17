from fastapi.testclient import TestClient
from main import app


client =  TestClient(app)


def test_pagamento_credit_card():
    payload = {
        "amount": 100.0,
        "method": "credit_card"
    }


    response = client.post("/pagamentos", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["original_amount"] == 100.0
    assert data["final_amount"] > 100.0
    assert data["method"] == "credit_card"
