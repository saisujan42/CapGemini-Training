from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("Concrete Method.")

class Child(Father):
    def disp(self):
        print("Child Class.")

def main():
    child = Child()
    child.disp()
    child.show()
main()