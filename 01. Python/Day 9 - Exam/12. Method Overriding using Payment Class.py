class Payment:
    def process_payemnt():
        print("Processing Your Payment...")
    
class CreditCardPayment(Payment):
    def process_payment(self):
        amount = float(input("Enter Amount : "))
        print(f"Successfully Processed ${amount} using Credit Card.")
    
class PayPalPayemnt(Payment):
    def process_payment(self):
        amount = float(input("Enter Amount : "))
        print(f"Successfully Processed ${amount} using PayPal.")

class BitCoinPayment(Payment):
    def process_payment(self):
        amount = float(input("Enter Amount : "))
        bitcoin = amount / 99114
        print("Successfully Processed ${amount} using Bitcoins.")
        print(f"{amount} = {bitcoin} Bitcoins")

def main():
    payments = {
        CreditCardPayment(),
        PayPalPayemnt(),
        BitCoinPayment(),
    }

    for payment in payments:
        payment.process_payment()
main()