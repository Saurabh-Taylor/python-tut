pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# methods::
# 1. get()
print(pizza.get('toppings', [])) # second argument is the default value
print(pizza.get('saurabh', "hey"))

# 2. keys(), 
# values(), 
# items() 
# clear()
# pop()
# popitem()
# update()
# - its a view object and its just a way to see the content of a dictionary without creating a separate copy of the data.
print(pizza.keys())
print(pizza.values())
print(pizza.items())

pizza.pop('price', 10) # second arg is the default value
pizza.popitem()
pizza.update({ 'price': 15, 'total_time': 25 })
