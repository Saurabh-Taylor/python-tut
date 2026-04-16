# age  = int(input("enter the age of the user: "))

# if age >=18  and age <= 40:
#     print(f'valid age for drinking is 20years old and yours is {age}, go champ have fun')
# elif age >= 50:
#     print(f' you are not having fun in your life')
# else: 
#     print('Stop wondering u can drink or not, go dumb study')


# ! Truthy And Falsy Values
# Few falsy values are: None, False, 0, 0.0, "", '', [], {}, set()

# print(False == False) 
# print(False == None) 
# print(False == 0)
# print(False == 0.0)
# print(False == '')

value = ''
if value:
    print("True")
else:
    print("False")

# ! Not operand
name = ""
if not name:
    print("Name is empty")

items = []
if not items:
    print("No items")


value = 0 # becoz 0 is falsy value
if not value:
    print("This runs!")

is_admin = False
if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
