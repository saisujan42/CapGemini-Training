import time
import functools

def log_execution(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Function {func.__name__}")
        print("Execution Time : ", end_time  - start_time)
        return result
    return wrapper

@log_execution
def add_numbers(a, b):
    time.sleep(1)
    product(45, 3)
    return a + b

@log_execution
def product(a, b):
    time.sleep(1)
    return a * b

add_result = add_numbers(5, 10)
product_result = product(5, 6)
print("Addition Result = ", add_result)
print("Product Result = ", product_result)