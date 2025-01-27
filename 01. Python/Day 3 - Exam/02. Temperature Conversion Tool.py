def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"Celsius to Fahrenheit = {fahrenheit}")

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    print(f"Celsius to Kelvin = {kelvin}")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(f"Fahrenheit to Celsius = {celsius}")

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print(f"Fahrenheit to Kelvin = {kelvin}")

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    print(f"Kelvin to Celsius = {celsius}")

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"Kelvin to Fahrenheit = {fahrenheit}")

# Checks if input is Float or Not to Validate Input
def is_float(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False  
    
# Calls Respective Conversion Functions based on Choice
def call_function(choice, temperature):
    match choice:
        case 1:
            celsius_to_fahrenheit(temperature)
        case 2:
            celsius_to_kelvin(temperature)
        case 3:
            fahrenheit_to_celsius(temperature)
        case 4:
            fahrenheit_to_kelvin(temperature)
        case 5:
            kelvin_to_celsius(temperature)
        case 6: 
            kelvin_to_fahrenheit(temperature)
        case _:
            exit()

# Gets Choice and inputs Temperature
# Also prompts user to provide input again in case of Invalid Input
def get_choice_and_convert():
    while True:
        print("Enter Choice \n1. Celsius to Fahrenheit \n2. Celsius to Kelvin \n3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin \n5. Kelvin to Celsius \n6. Kelvin to Fahrenheit")
        choice = input("Press Any Other Key to Exit : ")

        while not choice.isdigit():
            choice = input("Enter Choice Again : ")

        if int(choice) not in range(1, 7):
            exit()

        temperature = input("Enter Temperature : ")

        while not is_float(temperature):
            print("Invalid Input. Enter Valid Number.")
            temperature = input("Enter Temperature : ")

        call_function(int(choice), float(temperature))

def main():
    get_choice_and_convert()
main()