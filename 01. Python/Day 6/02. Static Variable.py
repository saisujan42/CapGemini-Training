class Example:
    name = "abc"

    def __init__(self):
        print("Current Name : ", Example.name)
    
    def modify_name(self):
        Example.name = input("Enter New Name : ")

    def print_name(self):
        print("Updated Name : ", Example.name)

def main():
    example = Example()
    example.modify_name()
    example.print_name()

    example.name = input("Enter New Name : ")       # This will Only Change static variable of Object
    Example.name = input("Enter New Name : ")       # This will Change the variable of the Class
    print("Update Name : ", Example.name)
main()