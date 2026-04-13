my_single_quote_string = 'Hello, Saurabh!'
print("Single Quote String:", my_single_quote_string)

my_multi_line_string = """
This is Multi Line String
what are u doin
"""
print(my_multi_line_string)

# escape sequence character - \
msg = 'It\'s a beautiful weather'
quote = "hey there, \"Hello World\""
print("msg::", msg)
print("quote::", quote)

# in - sometimes u need to check whether a specific word, letter is present in the string or not
my_specific_word = "hey saurabh, how are you doing"
print('hey' in my_specific_word) # True
# print('Hey' in my_specific_word) # False
# print('hey saurabh' in my_specific_word) # True
# print('hey saurabh, ' in my_specific_word) # True
# print('hey saurabh,' in my_specific_word) # True


# len() - how to get length of string
my_length_check_str = "saurabh is dashing guy"
print(len(my_length_check_str))

# to access a character at a particular index
my_character_check_str = "saurabh"
#  0  1  2  3  4  5  6 
# -7 -6 -5 -4 -3 -2 -1 
print(len(my_character_check_str))
print(my_character_check_str[0])
print(my_character_check_str[-1])


# ! Important Note: Strings are immutable in Python, which means that once a string is created, it cannot be modified.
# Many other programming languages group data types broadly as either primitive or reference types. 
# Primitive types are simple and immutable, meaning they can't be changed once declared. Reference types can hold multiple values, and are either mutable or immutable. 
# But Python doesn't draw a hard line between those two groups. Instead, all data gets treated as objects, 
# and some objects are immutable while others are mutable.

#Immutable data types can't be modified or altered once they're declared. You can point their variables at something new, which is called reassignment, but you can't change the original object itself by adding, removing, or replacing any of its elements.
#Strings are immutable data types in Python. This means that you can reassign a different string to a variable:
# ! A variable can be reassigned to a different string.
# greeting = 'hi'
# greeting = 'hello'
# print(greeting) # hello
