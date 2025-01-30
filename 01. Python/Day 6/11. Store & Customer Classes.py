class Customers:
    customers = {}

    def __init__(self):
        self.customer_id = input("Enter Customer ID : ")
        customer_details = {
            "customer_id": self.customer_id,
            "first_name": input("Enter First Name : "),
            "last_name": input("Enter Last Name : "),
            "phone_no": int(input("Enter Phone Number : ")),
            "email": input("Enter Email Address : "),
            "street": input("Enter Your Street : "),
            "city": input("Enter Your City : "),
            "state": input("Enter Your State : "),
            "zip_code": int(input("Enter ZipCode : ")),
        }
        Customers.customers[self.customer_id] = customer_details

    def get_customer_details(self, customer_id):
        return Customers.customers.get(customer_id, "Customer not found!")


class Orders:
    orders = {}

    def __init__(self, customer_id):
        if customer_id not in Customers.customers:
            print("Customer ID not found! Please register first.")
            return

        self.order_id = input("Enter Order ID : ")
        order_details = {
            "order_id": self.order_id,
            "customer_id": customer_id,
            "order_status": input("Enter Order Status : "),
            "order_date": input("Enter Order Date : "),
            "required_date": input("Enter Required Date : "),
            "shipped_date": input("Enter Shipped Date : "),
            "store_id": input("Enter Store ID : "),
            "staff_id": input("Enter Staff ID : "),
        }
        Orders.orders[self.order_id] = order_details

    def get_order_details(self, customer_id):
        customer_orders = []

        for order in Orders.orders.values():
            if order["customer_id"] == customer_id:
                customer_orders.append(order) 

        if customer_orders:
            return customer_orders
        else:
            return "No orders found for this customer."


def main():
    customers_instance = Customers()
    orders_instance = Orders("")

    while True:
        print("\n1. Register Customer")
        print("2. Place Order")
        print("3. Check Order Details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            customers_instance = Customers()  
        elif choice == "2":
            customer_id = input("Enter Customer ID: ")
            orders_instance = Orders(customer_id)  
        elif choice == "3":
            customer_id = input("Enter Customer ID to check orders: ")
            print(orders_instance.get_order_details(customer_id))  
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again!")
main()
