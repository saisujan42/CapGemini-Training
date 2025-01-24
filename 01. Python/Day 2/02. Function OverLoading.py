def display(name):
    print(f"Welcome {name}")

# The Second Function OverWrites the Previous Function With Same Name
def display(fname, lname):
    print(f"The Area is {fname} {lname}")

def main():
    display("Sujan")
    display("Davuluri", "Sujan")

main()