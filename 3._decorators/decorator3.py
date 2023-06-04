import time

def cache_decorator(func):
    cache = {} # Explain why dictionary
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"The function took {end_time - start_time} seconds to finish")
        return result
    return wrapper

@timer_decorator # Order matters
@cache_decorator
def calculate(n):
    return n ** 100

calculate(10)
calculate(10)
