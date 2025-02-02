class Animal:
    def speak(self):
        print("Animal Sound.")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Dog(Animal):
    def speak(self):
        print("Bark!")

def main():
    cat = Cat()
    dog = Dog()

    cat.speak()
    dog.speak()
main()