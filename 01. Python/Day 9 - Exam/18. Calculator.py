from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod    
    def subtract(self):
        pass
    
    @abstractmethod
    def multiply(self):
        pass
    
    @abstractmethod
    def divide(self):
        pass
    
class BasicCalculator(Calculator):
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        return num1 / num2

def main():
    calculator = BasicCalculator()

    print("Addition = ", calculator.add(5, 7))
    print("Subtraction = ", calculator.subtract(10, 3))
    print("Multiplication = ", calculator.multiply(5, 7))
    print("Division = ", calculator.divide(10, 5))
main()