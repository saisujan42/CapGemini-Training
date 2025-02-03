import queue
import time
import threading

def producer(q):
    for i in range(5):
        time.sleep(1)
        q.put(i)
        print("Produced = ", i)

def consumer(q):
    while True:
        item = q.get()
        if item == None:
            break
        print("Consumed = ", item)
        time.sleep(2)

def main():
    q = queue.Queue()
    producer_thread = threading.Thread(target = producer, args = (q,))
    consumer_thread = threading.Thread(target = consumer, args = (q,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    q.put(None)
    consumer_thread.join()

    print("Thread Communication Completed.")
main()