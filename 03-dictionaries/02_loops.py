products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

print(products)
# .values(), .keys(), and .items()

for item, price in products.items():
    products[item] = round(price * 0.8)

print(products)


for key, value in enumerate(products.items(), 1):
    print(key, value)