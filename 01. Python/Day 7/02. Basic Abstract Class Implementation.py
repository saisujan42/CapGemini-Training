from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        print("Animal Sound.")
    
class Dog(Animal):
    def make_sound(self):
        print("Bark.")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

def main():
    dog = Dog()
    cat = Cat()

    dog.make_sound()
    cat.make_sound()
main()