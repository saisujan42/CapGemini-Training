import threading
import time

def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has Acquired the Lock.")
        time.sleep(2)
        print(f"{threading.current_thread().name} has Released the Lock.")

def main():
    lock = threading.Lock()
    threads = [threading.Thread(target=task, args = (lock,))]

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
main()