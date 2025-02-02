class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Vehicle Brand : ", self.brand)
        print("Vehicle Model : ", self.model)

class Car(Vehicle):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def display_info(self):
        super().display_info()
        print("Car Top Speed : ", self.top_speed)

class Bike(Vehicle):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def display_info(self):
        super().display_info()
        print("Bike Top Speed : ", self.top_speed)

class ElectricCar(Car):
    def __init__(self, brand, model, top_speed, battery_capacity):
        super().__init__(brand, model, top_speed)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print("Battery Capacity : ", self.battery_capacity)

vehicle = Vehicle("Generic", "Model X")
car = Car("Skoda", "Slavia", "180 Km/Hr")
bike = Bike("Jawa", "42-FJ", "120 Km/Hr")
electric_car = ElectricCar("Tesla", "Model S", "100 Km/Hr", 100)

vehicle.display_info()
car.display_info()
bike.display_info()
electric_car.display_info()