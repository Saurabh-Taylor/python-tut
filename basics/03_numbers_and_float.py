
# ! Rest Mathematical Operations are same , there is new thing knowa as Floor Division

my_int = 56
my_int_2  = 12
print(my_int / my_int_2)
print(my_int // my_int_2) # 4 same as math.floor(56/12) 

# Sometimes, you might notice that the result of an operation involving floats has more decimal digits than expected. For example, the sum 0.1 + 0.2 equals 0.30000000000000004 instead of 0.3.
#This happens because numbers are stored in binary format, and some fractions cannot be represented exactly in binary. As a result, they are stored as finite approximations, in the same way the fraction 1/3 cannot be represented with a finite number of digits in decimal and is truncated after a certain number of its infinite digits (0.33333...).
# This leads to small rounding errors.
print(0.1 + 0.2)

# a. round
my_int_3 = 2.2 
my_int_4 = 2.5
print(round(my_int_3))
print(round(my_int_4))


# b. abs
my_int_5 = -4
print(abs(my_int_5))

