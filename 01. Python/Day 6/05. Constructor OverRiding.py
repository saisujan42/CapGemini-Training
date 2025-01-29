# First Constructor gets Overridden by Second Constructor
class Example:
    def __init__(self, name):
        print(f"First Constructor : Hello {name}")
    
    def __init__(self, age):
        print(f"Second Constructor : Age is {age}")

# Calls Only the Second Constructor
obj = Example(25)