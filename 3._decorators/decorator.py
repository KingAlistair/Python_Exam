def my_decorator(func):
    def wrapper():
        print("What does the dog say?")
        func()
        print("Yes that's right!")
    return wrapper

@my_decorator
def bark():
    print("Bark bark!")

bark()
