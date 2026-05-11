from functools import wraps

def my_generator(func):
    @wraps(func) # becoz of this i will preserve my function
    def wrapper():
        print("before function starts")
        func()
        print("after function starts")

    return wrapper

@my_generator
def greet():
    print("Hello From generator function")

greet()
print(greet.__name__)