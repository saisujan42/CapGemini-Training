class Car:
    def __init__(self, car_name):
        self.car_name = car_name

    def move(self):
        print(f"{self.car_name} drives on the road.")

class Airplane:
    def __init__(self, plane_name):
        self.plane_name = plane_name

    def move(self):
        print(f"{self.plane_name} flies in the Sky.")

class FlyingCar(Car, Airplane):
    def __init__(self, fc_name):
        Car.__init__(self, fc_name)
        Airplane.__init__(self, fc_name)

    def move(self, mode):
        if mode == "fly":
            Airplane.move(self)  
        else:
            Car.move(self)  

def main():
    flying_car = FlyingCar("Smart Car")

    flying_car.move("drive")        
    flying_car.move("fly")   
main()