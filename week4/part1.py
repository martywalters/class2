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

def run_synchronously():
    start_time = time.perf_counter()
    global result_add
    global result_subtract
    global result_multiply
    global result_divide
    global result_modulus

    result_add = add(10, 5)
    result_subtract = subtract(20, 7)
    result_multiply = multiply(8, 4)
    result_divide = divide(30, 6)
    result_modulus = modulus(25, 7)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Synchronous time took {elapsed_time:.2f} seconds.")

def run_concurrently():
    global add_result
    global sub_result
    global mult_result
    global div_result
    global mod_result
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as exec:
        add_result = exec.submit(add, 10,5)
        sub_result = exec.submit(subtract,20,7)
        mult_result = exec.submit(multiply,8,4)
        div_result = exec.submit(divide,30,6)
        mod_result = exec.submit(modulus,25,7)
        
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Concurrent time took {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
                   
    run_synchronously()
    run_concurrently()
    print("\nResults:")
    print(f"Addition:\t {result_add} (synchronous) vs {add_result.result()} (concurrent)")
    print(f"Subtraction:\t {result_subtract} (synchronous) vs {sub_result.result()} (concurrent)")
    print(f"Multiplication:\t {result_multiply} (synchronous) vs {mult_result.result()} (concurrent)")
    print(f"Division:\t {result_divide} (synchronous) vs {div_result.result()} (concurrent)")
    print(f"Modulus:\t {result_modulus} (synchronous) vs {mod_result.result()} (concurrent)")



