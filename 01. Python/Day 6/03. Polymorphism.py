class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def main():
    for animal in [Cat(), Dog()]:
        animal.sound()
main()