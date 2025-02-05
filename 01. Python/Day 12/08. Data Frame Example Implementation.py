import csv
import pandas as pd

def initialize_csv(csv_file):
    headers = ["Customer ID", "Customer Name", "Product"]
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def add_to_csv(csv_file, customer_id, customer_name, product):
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([customer_id, customer_name, product])

def convert_to_data_frame(csv_file):
    df = pd.read_csv(csv_file)
    print(df)

def get_input(csv_file):
    print()
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    product = input("Enter Product Purchased: ")
    add_to_csv(csv_file, customer_id, customer_name, product)

def main():
    csv_file = "customers.csv"
    initialize_csv(csv_file)

    while True:
        choice = input("1. To Enter Details \n2. Exit \nEnter choice: ")
        if choice == "1":
            get_input(csv_file)
        elif choice == "2":
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

    convert_to_data_frame(csv_file)
main()