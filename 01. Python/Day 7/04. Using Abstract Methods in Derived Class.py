from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Enter Length : "))
        self.breadth = int(input("Enter Breadth : "))
    
    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self):
        self.radius = int(input("Enter Radius : "))
    
    def area(self):
        return 3.14 * self.radius ** 2

def main():
    rectangle = Rectangle()
    print("Area of Rectangle : ", rectangle.area())
    
    circle = Circle()
    print("Area of Circle : ", circle.area())
main()