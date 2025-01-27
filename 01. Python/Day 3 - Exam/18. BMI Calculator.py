# Prints the BMI Category
def print_category(bmi_value):
    if bmi_value < 18.5:
        print("Underweight")
    elif bmi_value >= 18.5 and bmi_value < 25:
        print("Normal")
    elif bmi_value >= 25 and bmi_value < 30:
        print("Overweight")
    elif bmi_value >= 30:
        print("Obese")

# Calculates BMI Using Formula
# BMI = Weight/ (Height * Height)

def find_bmi(height, weight):
    return weight / (height * height)

# Takes Height and Weight as Input
# Prompts User to Enter Correct Values in case of Invalid Input

def get_input():
    height = float(input("Enter Height in Metres(m): "))
    while height <= 0:
        print("\nInvalid Input. Enter Positive Value.")
        height = float(input("Enter Height in Metres(m): "))
    
    weight = float(input("Enter Weight in Kilograms(kg): "))
    while weight <= 0:
        print("\nInvalid Input. Enter Positive Value.")
        weight = float(input("Enter Weight in Kilograms(kg): "))
    
    return (height, weight)

def main():
    (height, weight) = get_input()
    bmi_value = find_bmi(height, weight)
    print_category(bmi_value)
main()