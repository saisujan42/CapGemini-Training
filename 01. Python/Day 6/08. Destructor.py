class DestructorExample:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} is Created.")
    
    def __del__(self):
        print(f"Object {self.name} is Destroyed.")

obj = DestructorExample("Sample")
del obj