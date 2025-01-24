import math
a, b, c = map(int, input("Enter Co-Efficients of Quadratic Equation: ").split())
Root1 = ((-b) + (math.sqrt(b*b - 4*a*c))) / (2*a)
Root2 = ((-b) - (math.sqrt(b*b - 4*a*c))) / (2*a)
print(Root1, Root2)