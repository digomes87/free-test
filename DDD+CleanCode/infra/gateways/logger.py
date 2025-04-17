

def log_payment(method: str, amount: float, final_amount: float):
    print(f"[LOG] Pagamento via {method.upper()}: R$ {amount: 2f} -> R$ {final_amount: 2f}")
