import time
import concurrent.futures

# Define the five functions
def add(x, y):
    time.sleep(1)
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
def func(secs):
    print('in func')
    time.sleep(secs)
    return('done' , secs)

def run_synchronously():
    start_time = time.perf_counter()

    # Call each function sequentially
    result_add = add(10, 5)
    result_subtract = subtract(20, 7)
    result_multiply = multiply(8, 4)
    result_divide = divide(30, 6)
    result_modulus = modulus(25, 7)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Synchronous execution took {elapsed_time:.2f} seconds.")

def run_concurrently():
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as exec:
        add_result = exec.submit(add, 1 ,2)
        sub_result = exec.submit(subtract,7,2)
        mult_result = exec.submit(multiply(8, 4))
        div_result = exec.submit(divide(30, 6))
        mod_result = exec.submit(modulus(25, 7))
        

    
    #print(add_result.result())
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Concurrent execution took {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    run_synchronously()
    run_concurrently()

