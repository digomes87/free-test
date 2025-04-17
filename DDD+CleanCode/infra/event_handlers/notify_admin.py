from domain.events.payment_event import PaymentCompleted


def notify_admin(event: PaymentCompleted):
    print(f"Admin pagamento via {event.method}")
