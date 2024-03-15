import time
import multiprocessing
from functools import partial

# Define the functions
def add(x, y):
    time.sleep(1)
    print('add')
    return x + y

def subtract(x, y):
    time.sleep(1)
    return x - y

def multiply(x, y):
    time.sleep(1)
    return x * y

def divide(x, y):
    time.sleep(1)
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

def modulus(x, y):
    time.sleep(1)
    return x % y

# Synchronous execution
def run_synchronously():
    start_time = time.time()
    result_add = add(10, 5)
    result_subtract = subtract(20, 7)
    result_multiply = multiply(8, 3)
    result_divide = divide(30, 6)
    result_modulus = modulus(25, 4)
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time:.2f} seconds")
    return result_add, result_subtract, result_multiply, result_divide, result_modulus

# Concurrent execution
def run_concurrently():
    start_time = time.time()
    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(partial(add, y=5), [10, 20, 8, 30, 25])
    end_time = time.time()
    print(f"Concurrent execution time: {end_time - start_time:.2f} seconds")
    return tuple(results)

if __name__ == "__main__":
    result_sync = run_synchronously()
    result_concurrent = run_concurrently()

    print("\nResults:")
    print(f"Addition: {result_sync[0]} (synchronous) vs {result_concurrent[0]} (concurrent)")
    print(f"Subtraction: {result_sync[1]} (synchronous) vs {result_concurrent[1]} (concurrent)")
    print(f"Multiplication: {result_sync[2]} (synchronous) vs {result_concurrent[2]} (concurrent)")
    print(f"Division: {result_sync[3]} (synchronous) vs {result_concurrent[3]} (concurrent)")
    print(f"Modulus: {result_sync[4]} (synchronous) vs {result_concurrent[4]} (concurrent)")
