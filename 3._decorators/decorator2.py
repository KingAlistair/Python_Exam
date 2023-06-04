import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"The function took {end_time - start_time} seconds to finish")
        return result
    return wrapper

@timer_decorator
def calculate(n):
    return n ** 10 
    
print("Result: ", calculate(10))