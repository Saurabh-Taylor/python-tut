from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_activity

def brew_chai(type, milk = "no"):
    print(f"Brewing {type}")

brew_chai("Masala Chai")