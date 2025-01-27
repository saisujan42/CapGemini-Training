# Inputs Item Name and Cost
# Takes Dictionary and bill amount as parameters
# Adds new item to dictionary and updates bill amount
def add_items(cart_items, bill_amount):
    item_name = input("\nEnter Item Name : ")
    item_cost = int(input("Enter Item Cost : "))

    while item_cost < 0:
        print("Invalid Input. Enter Positive Cost.")
        item_cost = int(input("Enter Item Cost Again : "))

    if item_name in cart_items:
        cart_items[item_name] += item_cost
    else:
        cart_items[item_name] = item_cost

    bill_amount += item_cost     # Calculate Total Bill to Decrease Time Complexity
    return bill_amount

# Takes dictionary as parameter
# Prints the Key-Value Pairs
def view_items(cart_items):
    print("\nYour Cart Items Include : ")

    for item, cost in cart_items.items():
        print(f"{item} = {cost}")

# Prints the total bill value
def total_bill(bill_amount):
    print(f"\nThe Total Bill Amount = {bill_amount}")
    
# Takes Input By Asking Choice
# Using match statement to call respective functions
def get_input():
    cart_items = {}
    bill_amount = 0

    while True:
        choice = int(input("Enter\n 1. To Add Items\n 2. View Items\n 3. Calculate Total Bill\n 4. Exit : "))

        match choice:
            case 1:
                bill_amount = add_items(cart_items, bill_amount)
            case 2:
                view_items(cart_items)
            case 3: 
                total_bill(bill_amount)
            case 4: 
                print("You Have Exited Successfully")
                exit()


def main():
    get_input()
main()