from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        print("The Vehicle Brand is : ", brand)

    @abstractmethod
    def max_speed():
        pass

class Car(Vehicle):
    def max_speed(self):
        print("Car Speed is 200 Km/Hr")

class Bike(Vehicle):
    def max_speed(self):
        print("Bike Speed is 150 Km/Hr")

def main():
    car = Car("Skoda")
    car.max_speed()
    
    bike = Bike("Jawa")
    bike.max_speed()
main()