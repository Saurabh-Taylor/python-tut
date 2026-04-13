my_int = -4
print("my_int::", my_int)
print("type my_int::", type(my_int))

my_float = -1.5
print("my_float::", my_float)
print("type my_float::", type(my_float))


my_string = "Hello, Saurabh!"
print("my_string::", my_string)

my_boolean = True
print("my_boolean::", my_boolean)


# Set - An unordered collection of unique elements,
my_set = { # this is set literal 
    "apple",
    "banana",
    1,
    4.5,
    1 # Duplicate element, will be ignored in the set
}

my_set_2 = set(("saurabh", "this", "set")) # this is set constrctor
print("my_set::", my_set)
print("my_set_2::", my_set_2)

# Dictionary (object) - Key-value pairs, where keys are unique and values can be of any data type.
my_dictionary = {
    "name": "Saurabh",
    "age": 30,
    "city": "New York"
}
print("my_dictionary::", my_dictionary)

my_tuple = (1, 2, 3, "Hello", 4.5)
print("my_tuple::", my_tuple[3])
# Difference between tuple and set
# 1. tuples are immutable, sets are mutable
# 2. tuples are ordered, sets are unordered
# 3. tuples allow duplicates, sets don't
# 4. tuples are faster for iteration and indexing, sets use hash tables internally.


# range - sequence of numbers, often used in loops
my_range = range(5)
print("my_range::", my_range) #(0, 5)

# List - An ordered collection of elements that supports different data types. 
my_list = [22, "hello world", 3.14, False]
print("my_list::", my_list)

# None - A special value that represents the absence of a value.
my_none = None
print("my_none::", my_none)

# type - to get the data type of a variable
print(type(my_int))
print(type(my_float))

# isinstance - function lets you check if a variable matches a specific data type
isStr = isinstance("Saurabh is here", str)
print("isStr::", isStr)

isint = isinstance(1, float)
print("isint::", isint)

developer = 'Naomi'

result = developer.endswith('N') # ?
print(result)
print(3.14 + 1)


def greet():
    pass

greet()