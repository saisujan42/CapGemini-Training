class Customers:
    def __init__(self):
        self.customer_id = input("Enter Customer ID : ")
        self.first_name = input("Enter First Name : ")
        self.last_name = input("Enter Last Name : ")
        self.phone_no = int(input("Enter Phone Number : "))
        self.email = input("Enter Email Address : ")
        self.street = input("Enter Your Street : ")
        self.city = input("Enter Your City : ")
        self.state = input("Enter Your State : ")
        self.zip_code = int(input("Enter ZipCode : "))
    
    def print_customer_details(self):
        print("Customer ID : ", self.customer_id)
        print("First Name : ", self.first_name)
        print("Last Name : ", self.last_name)
        print("Phone Number : ", self.phone_no)
        print("Email Address : ", self.email)
        print("Street : ", self.street)
        print("City : ", self.city)
        print("State : ", self.state)
        print("Zip Code : ", self.zip_code)
    
class Orders:
    def __init__(self, customer):
        self.order_id = input("Enter Order ID : ")
        self.order_status = input("Enter Order Status : ")
        self.order_date = input("Enter Order Date : ")
        self.required_date = input("Enter Required Date : ")
        self.shipped_date = input("Enter Shipped Date : ")
        self.store_id = input("Enter Store ID : ")
        self.staff_id = input("Enter Staff ID : ")