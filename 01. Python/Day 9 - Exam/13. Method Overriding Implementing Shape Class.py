class Shape:
    def area(self, shape):
        print(f"Area of {shape} = ", end = '')
    
class Triangle(Shape):
    def area(self, breadth, height):
        super().area("Triangle")
        print(0.5 * breadth * height)
    
class Square(Shape):
    def area(self, side):
        super().area("Square")
        print(side * side)

def main():
    triangle = Triangle()
    square = Square()

    triangle.area(5, 7)
    square.area(5)
main()