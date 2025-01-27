# Prints Grade Based on Percentage
# By Using if-elif-else conditional statements
def calculate_grade(name, percentage):
    if percentage >= 85:
        print(f"Grade of {name} = O")
    elif percentage < 85 and percentage >= 70:
        print(f"Grade of {name} = A")
    elif percentage < 70 and percentage >= 60:
        print(f"Grade of {name} = B")
    elif percentage < 60 and percentage >= 50:
        print(f"Grade of {name} = C")
    elif percentage < 50 and percentage >= 40:
        print(f"Grade of {name} = D")
    else:
        print(f"Grade of {name} = Fail")

# Calculate percentage and prints the answer
# Calls another fucntion to print grade
def calculate_percentage_and_grade(name, total_marks):
    print(f"Total Marks Of {name} = {total_marks}")
    
    percentage = total_marks / 5
    print(f"Percentage of {name} = {percentage}")

    calculate_grade(name, percentage)

# Gets input and validates input
# Uses while loop to prompt user until valid input is given
def get_input():
    name = input("Enter Student Name : ")
    total_marks = 0

    for i in range(5):
        score = input(f"Enter Marks in Subject {i + 1} : ")

        while not score.isdigit() or int(score) < 0:
            print("Invalid Input. Enter A Positive Value : ")
            score = input(f"Enter Marks in Subject {i + 1} : ")
        
        total_marks += int(score)
    
    return (name, total_marks)

def main():
    (name, total_marks) = get_input()
    calculate_percentage_and_grade(name, total_marks)

main()