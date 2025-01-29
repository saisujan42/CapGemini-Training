# Use Single Quotations for Kwargs
class Example:
    def __init__(self, **kwargs):
        if 'name' in kwargs and 'age' in kwargs:
            print(f"Hello {kwargs['name']}, You are {kwargs['age']} Years Old.")
        elif 'name' in kwargs:
            print(f"Hello {kwargs['name']}")
        self.xfield = kwargs['name']

obj1 = Example(name = 'Alice')
obj2 = Example(name = 'Bob', age = 30)
print(obj2.xfield)