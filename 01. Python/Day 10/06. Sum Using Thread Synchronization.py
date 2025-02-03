import threading

def process_sum(chunk):
    result = sum(chunk)
    print("Result = ", result)

def main():
    data_chunks = [
        list(range(10000)),
        list(range(10000, 20000)),
        list(range(20000, 30000))
    ]

    threads = []
    for chunk in data_chunks:
        thread = threading.Thread(target = process_sum, args = (chunk,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
main()