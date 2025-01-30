from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("Concrete Method.")

class Son(Father):
    def disp(self):
        print("Son is Implementing the Abstract Method.")
    
class Daughter(Father):
    def disp(self):
        print("Daughter is Implementing the Abstract Method.")

def main():
    son = Son()
    son.disp()
    son.show()

    daughter = Daughter()
    daughter.disp()
    daughter.show()
main()