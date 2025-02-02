class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def check_availability(self, quantity):
        if quantity <= self.stock:
            print("Stock is Available")
        else:
            print("Stock is Unavailable")
        return False

def main():
    product = Product("Bottle", 200, 5000)
    product.check_availability(500)
    product.check_availability(6000)
main()