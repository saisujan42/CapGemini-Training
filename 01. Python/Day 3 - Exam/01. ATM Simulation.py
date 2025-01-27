# Checks if input is Float or Not to Validate Input
def is_float(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False  

# Takes Input for Deposit Money
# Adds to Account Balance and returns it
def deposit_money(account_balance):
    deposit = input("Enter Deposit Value : ")

    while not is_float(deposit) or float(deposit) < 0:
        print("\nInvalid Input.")
        deposit = input("Enter Deposit Value : ")
    
    account_balance += float(deposit)
    return account_balance

# Takes Input for Withdrawal Money
# Subtracts from Account Balance and returns it
def withdraw_money(account_balance):
    withdraw = input("Enter Withdrawal Value : ")

    while not is_float(withdraw) or float(withdraw) < 0:
        print("\nInvalid Input.")
        withdraw = input("Enter Withdrawal Value : ")
    
    if float(withdraw) > account_balance:
        print("Insufficient Account Balance")
        return account_balance
    
    account_balance -= float(withdraw)
    return account_balance

# Print Account Balance
def check_balance(account_balance):
    print(f"\nYour Account Balance = {account_balance}")
    return account_balance

# Call Respective Functions based on User Choice
def perform_actions(choice, account_balance):
    match choice:
        case 1:
            return deposit_money(account_balance)
        case 2:
            return withdraw_money(account_balance)
        case 3:
            return check_balance(account_balance)

# Gets User choice until input is given
# Exits if Any Other Value is entered by user
def get_choice_and_perform_actions():
    account_balance = 0

    while True:
        print("Enter \n1. Deposit Money \n2. Withdraw Money \n3. Check Balance \nPress Any Character to Exit : ")
        choice = input()

        while not choice.isdigit():
            print("\nInvalid Input. Enter Choice Again : ")
            choice = input()

        if int(choice) not in range(1, 4):
            exit()
    
        account_balance = perform_actions(int(choice), account_balance)

def main():
    get_choice_and_perform_actions()
main()