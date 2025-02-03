import threading

def print_even():
    for i in range(0, 11, 2):  
        print(f"Even: {i}")

def print_odd():
    for i in range(1, 11, 2):  
        print(f"Odd: {i}")

even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Finished printing odd and even numbers.")