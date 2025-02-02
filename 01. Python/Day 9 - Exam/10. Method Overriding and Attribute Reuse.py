class Electronics:
    def __init__(self, brand, battery_power):
        self.brand = brand
        self.battery_power = battery_power  

    def device_info(self):
        print("Brand Name:", self.brand)
        print("Battery Power:", self.battery_power, "W")

class MobileDevice(Electronics):
    def __init__(self, brand, battery_power, cost):
        super().__init__(brand, battery_power)  
        self.cost = cost  

    def device_info(self):
        super().device_info()
        print("Cost:", self.cost, "INR")

class SmartPhone(MobileDevice):
    def __init__(self, brand, battery_power, cost, os_version):
        super().__init__(brand, battery_power, cost)  
        self.os_version = os_version

    def device_info(self):
        super().device_info()
        print("OS Version:", self.os_version)

def main():
    smartphone = SmartPhone("Samsung", 25, 25000, "Android 13")  
    smartphone.device_info()
main()
