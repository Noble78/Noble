class Payment:
    def process_payment(self, amount):
        return f"Payment of ${amount} processed successfully"


payment = Payment()

print(payment.process_payment(100))