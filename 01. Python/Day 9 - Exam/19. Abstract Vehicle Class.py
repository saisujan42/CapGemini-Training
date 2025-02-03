from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        print("Starting Engine...")

    @abstractmethod
    def stop_engine(self):
        print("Stopping Engine...")

class Bike(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Bike Engine has been Started.")
        print()
    
    def stop_engine(self):
        super().stop_engine()
        print("Bike Engine has been Stopped.")
        print()

class Car(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Car Engine has been Started.")
        print()
    
    def stop_engine(self):
        super().stop_engine()
        print("Car Engine has been Stopped.")
        print()

class Truck(Vehicle):
    def start_engine(self):
        super().start_engine()
        print("Truck Engine has been Started.")
        print()
    
    def stop_engine(self):
        super().stop_engine()
        print("Truck Engine has been Stopped.")
        print()

def main():
    bike = Bike()
    car = Car()
    truck = Truck()

    bike.start_engine()
    bike.stop_engine()

    car.start_engine()
    car.stop_engine()

    truck.start_engine()
    truck.stop_engine()
main()