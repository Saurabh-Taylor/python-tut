# arguments - position, keywords, *args, ** kwargs
# Q1:

# def f(a, b=2, *args, **kwargs):
#     print(a, b, args, kwargs)
# f(1, 3, 5, 7, x=10)


# Q2:
# def f(a, b):
#     pass
# f(b=2, 1)

#1 - 1, 3, (5, 7), {"x": 10}
#2 - positional args cant be appear after keyword args
#3 - no idea to it
# 4.[1] and [1, 2]

# def d(x, lst=None):
#     if(lst is None):
#         lst = []
#     lst.append(x)
#     return lst
   
# print(d(1))
# print(d(2))

# recursive function


def count(n):
       print(n)
       count(n - 1) 

count(3) 

















# lambda functions
# documenting and built-in functions
# python imports, modules, __init__.py

