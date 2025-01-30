from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def PanCardNumber(self):
        print("Father Pan Number : 1234")

class Son(Father):
    def PanCardNumber(self):
        # You Can Call the Abstract Method using Super Keyword
        super().PanCardNumber()
        print("Son Pan Number : 5678")
    
class Daughter(Father):
    def PanCardNumber(self):
        print("Daughter Pan Number : 9321")

def main():
    son = Son()
    daughter = Daughter()
    
    son.PanCardNumber()
    daughter.PanCardNumber()
main()