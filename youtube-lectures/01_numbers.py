# whenever we do calculations like 4 + 5.45 = it is an industry standard to make the data type explicitly same, as it matters a lot in finance and banking application

print(type(str(2.23)))

my_text = 'She said "hi"'
print(repr(my_text))

print(str(my_text))
print(my_text)

# Math Library
import math
math.floor(3.14)

# >>> math.trunc(-3.4)
# -3
# >>> math.floor(-3.4)
# -4

# Random Library
import random
print(random.random())
print(random.randint(0,10)) # --> gives random integer from 0 to 9
l1 = ["saurabh", "Gk", "Mahesh"]
print(random.choice(l1))
print(random.shuffle(l1)) # --> will change existing list 

# Decimal libary
from decimal import Decimal
Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")

from fractions import Fraction
Fraction(2,1)

# set data type
setone =  {1,2,3,4}
settwo = {2,3,4}

print(setone & settwo) # intersection
print(setone | settwo) # union




