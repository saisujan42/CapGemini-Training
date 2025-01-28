class Parent:
    def __init__(self):
        self.BigNose = "7CM"

    def display_parent(self):
        print("This is the Parent Class.")

class Child(Parent):
    # super Keyword Overrides the Parent Class Constructor
    def __init__(self):
        super().__init__()
        print("This is Child Class Constructor.")

    def display_child(self):
        print("This is the Child Class.")

child = Child()
child.display_parent()
child.display_child()
print(child.BigNose)