from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def Profession(self):
        pass        
    def Introduce(self):
        print(f"The person is {self.Profession()}")

class Engineer(Person):
    def Profession(self):
        return "Engineer"

class Doctor(Person):
    def Profession(self):
        return "Doctor"

def main():
    engineer = Engineer()
    engineer.Introduce()

    doctor = Doctor()
    doctor.Introduce()
main()