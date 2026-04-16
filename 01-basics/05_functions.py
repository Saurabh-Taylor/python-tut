def greeting():                 # in js - function greeting() {}
    print("Hello, Saurabh!")


# ! Scope in Python and How Does It Work?

# To correctly determine scope, Python follows the LEGB rule, which stands for the following:
# Local scope (L): Variables defined in functions or classes.
# Enclosing scope (E): Variables defined in enclosing or nested functions.
# Global scope (G): Variables defined at the top level of the module or file.
# Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.


# 1. Local Scope
def myFunc():
    my_name = "saurabh"
    print(my_name)

myFunc()


# global variable keyword and there is nonlocal keyword
my_var = 10

def change_var():
    global my_var 
    my_var = 20

change_var()
