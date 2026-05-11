from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_type):
        if user_type != "admin":
            print("Access Denied: Admins Only")
            return None
        else:
            return func(user_type)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Access Granted to tea inventory")

access_tea_inventory("user")
access_tea_inventory("admin")