class Bird:
    def fly(self):
        return "This Bird can Fly."

class Mammal:
    def walk(self):
        return "This Mammal can Walk."

class Bat(Bird, Mammal):
    def sleep(self):
        return "Bat can Sleep Upside Down."

def main():
    bat = Bat()
    print(bat.fly())
    print(bat.walk())
    print(bat.sleep())
main()