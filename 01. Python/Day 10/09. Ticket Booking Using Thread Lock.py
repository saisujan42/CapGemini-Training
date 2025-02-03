import threading
import time

class TicketBooking:
    def __init__(self, available_tickets):
        self.available_tickets = available_tickets
        self.lock = threading.Lock()    # Lock object
    
    def book_ticket(self, name):
        print(f"{name} is Trying to Book a Ticket...")
        with self.lock:
            if self.available_tickets > 0:
                time.sleep(1)
                self.available_tickets -= 1
                print(f"{name} Successfully Booked a Ticket!")
                print(f"Remaining Tickets = {self.available_tickets}")
            else:
                print(f"Sorry {name}, No Tickets Available!")

def main():
    booking_system = TicketBooking(1)

    threads = []
    users = ["Alice", "Bob"]

    for user in users:
        t = threading.Thread(target = booking_system.book_ticket, args = (user,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
main()