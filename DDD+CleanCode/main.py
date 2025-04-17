# from decimal import Decimal
# from application.use_cases.process_payment import PaymentProcessor
# from domain.services.strategies import PixPayment, CreditCardPayment, BoletoPayment
# from infra.gateways.logger import log_payment
#
#
# if __name__ == "__main__":
#     amount = Decimal("200")
#     payment = PaymentProcessor(CreditCardPayment())
#     final = payment.execute(amount)
#     log_payment("Cartão", float(amount), float(final))

from decimal import Decimal

from infra.container import container
from domain.events.payment_event import PaymentCompleted
from infra.event_bus import subscribe, publish
from infra.event_handlers.notify_admin import notify_admin
from infra.event_handlers.webhook import send_webhook
from infra.repositories.in_memory import InMemoryPaymentRepository

# 1. Subscrição dos eventos
subscribe(PaymentCompleted, notify_admin)
subscribe(PaymentCompleted, send_webhook)

# 2. Resolve o serviço via container
payment_processor = container.resolve("credit_card")
repository = InMemoryPaymentRepository()

# 3. Executa o pagamento
amount = Decimal("200")
final_amount = payment_processor.execute(amount)

# 4. Persiste no repositório fake
repository.save("credit_card", amount, final_amount)

# 5. Publica evento de domínio
event = PaymentCompleted(amount=amount, final_amount=final_amount, method="credit_card")
publish(event)

