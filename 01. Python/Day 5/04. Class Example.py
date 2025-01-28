class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"This Car is a {self.brand} {self.model}")
    
car1 = Car("Toyota", "Corolla")
car2 = Car("Skoda", "Slavia")
car1.display_info()
car2.display_info()