from domain.events.payment_event import PaymentCompleted


def send_webhook(event: PaymentCompleted):
    print(f"Enviado evento: {event}")
