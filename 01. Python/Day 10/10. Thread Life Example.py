import threading
import time

def task():
    while True:
        print("Thread is Running...")
        time.sleep(1)

daemon_thread = threading.Thread(target = task, daemon = True)
daemon_thread.start()

time.sleep(3)
print("Main Thread Exiting.")