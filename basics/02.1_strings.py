
# ! 1. String concatenation
my_str_1 = "Hey"
my_str_2 = 'Saurabh'
# print(my_str_1 + ' ' + my_str_2 + ' ' + 'How are You?')

name = "saurabh"
age = 20
# print(name + str(age))

name = 'saurabh'
age = 26
name_and_age = name
# print("before name_and_age::", name_and_age)
name_and_age += str(age)
# print("after name_and_age::", name_and_age)


# ! 2. String Interpolation
# The process of inserting variables and expressions into a string is called string interpolation. (template literals)
# Python has a category of string called f-strings (short for formatted string literals), which allows you to handle interpolation with a compact and readable syntax.

name = "Hercules"
age = 100
name_and_age = f'My name is {name} and age is {str(age)} '
# print(name_and_age)


# ! 3. String Slicing And How Does it Work?
my_str = "Hello World"
#  0   1   2  3  4  5  6  7  8  9 10
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# print(my_str[0]) # H
# print(my_str[1]) # e
# print(my_str[-5]) # W
# print(my_str[-3]) # r

# string[start:stop]
# print(my_str[0:4])
# print(my_str[:7])  # start will be by default to 0 in this case
# print(my_str[8:])  # in this it will go the end becoz we did not mentioned stop index
# print(my_str[:])  # Hello world
# ! Note that slicing a string does not modify the original string becoz string is immutable

# Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice.
# string[start:stop:step]
# In the example below, the slicing starts at index 0, stops before 11, and takes every second character:
my_str = 'Hello world'
# print(len(my_str))
# print(my_str[6])
# print(my_str[0:11:2]) # Hlowrd
# ! step = 2 → take every 2nd character

# Q. TODO: How to reverse a string?
# print(my_str[::-1])
# print(my_str[-1:-4]) # this will give empty string becoz step by default runs from left to right
# print(my_str[-1:-4:-1]) # thats why we have to tell that start from right


# Some Common String Methods:
my_str = "  Hello World  "
# 1. str.strip() {trim() in js } - removes leading and trailing whitespace from the string.
print(my_str.strip())

my_str = "Hello World"
# 2. str.upper() - converts all characters in the string to uppercase.
print(my_str.upper())
# 3. str.lower() - converts all characters in the string to lowercase.
print(my_str.lower())

# 4. str.replace(old, new) - replaces all occurrences of the old substring with the new substring.
replaced_my_str = my_str.replace('Hello', 'hi')
print(replaced_my_str)

# 5. str.split(separator) - splits the string into a list of substrings based on the specified separator.
print(my_str.split(' '))

# 6. separator.join(iterable) - joins the elements of an iterable (like a list) into a single string, using the string as a separator.
My_list = ['Hello', 'World']
print('-'.join(My_list))  # Output: Hello, World -> will join the list of strings

# 7. str.find(substring) - returns the lowest index of the substring if it is found in the string, otherwise returns -1.
print(my_str.find('World')) # - output -> 4 (index of first occurrence of '

# 8. str.count('0') - Returns the number of times a substring appears in a string.
print(my_str.count('S'))

# 9. str.capitalize() - Returns a copy of the string with the first character capitalized and the rest lowercased.
print(my_str.capitalize()) # Hello world

# 10. str.title() - Returns a copy of the string with the first character of each word capitalized and the rest lowercased.
print(my_str.title()) # Hello World

# 11. str.isupper() - Returns True if all characters in the string are uppercase, otherwise returns False.
print(my_str.isupper()) # False 

# 12. str.islower() - Returns True if all characters in the string are lowercase, otherwise returns False.
print(my_str.islower()) # False


