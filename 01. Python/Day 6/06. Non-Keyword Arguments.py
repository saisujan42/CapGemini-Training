class Example:
    def __init__(self, *args):
        if len(args) == 1:
            print(f"Hello {args[0]}")
        elif len(args) == 2:
            print(f"Hello {args[0]}, you are {args[1]} Years Old")

obj = Example("Hari", 20)