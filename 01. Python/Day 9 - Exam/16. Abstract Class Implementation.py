from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self, shape):
        print(f"Area of {shape} : ", end = '')

class Circle(Shape):
    def area(self, radius):
        super().area("Circle")
        print(3.14 * radius * radius)

class Rectangle(Shape):
    def area(self, length, breadth):
        super().area("Rectangle")
        print(length * breadth)

def main():
    circle = Circle()
    rectangle = Rectangle()

    circle.area(7)
    rectangle.area(5, 9)
main()