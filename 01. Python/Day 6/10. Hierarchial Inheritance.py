# Parent Class
class Shape:
    def area(self):
        pass

# Child Class 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Child Class 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
def main():
    circle = Circle(7)
    square = Square(5)

    print("Area of Circle : ", circle.area())
    print("Area of Square : ", square.area())
main()