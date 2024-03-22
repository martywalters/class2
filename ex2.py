from concurrent.futures import ThreadPoolExecutor

def my_function():
    print("Thread is running!")

with ThreadPoolExecutor(max_workers=5) as executor:
    future = executor.submit(my_function)
    # You can submit more tasks here

# The ThreadPoolExecutor automatically manages the thread pool
