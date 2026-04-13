developer = ["saurabh", 23, "full stack developer", "Saurabh"]

# 1.Delete
del developer[0]
# print(developer)

# 2. element is inside list or not
# print('Saurabh' in developer)

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
# print(developer[2][1])

# unpacking

name, age, language = developer
# print("name::", name)
# print("age::", age)
# print("language::", language)


name, *rest = developer

# print("name::", name)
# print("rest::", rest)

numbers = [1, 2, 3, 4, 5, 6]
# print(numbers[1::2])



my_list = [1,2,3,4]
my_list_2 = [5,6,7]

# append -> add item at the end 
my_list.append(my_list_2)

# insert -> it will insert an element at specific index
my_list.insert(1, 10)

# extend -> it will append individual 
my_list.extend(my_list_2)

# remove -> id you want to remove an element from a list, only remove first occurence
my_list.remove(10)

# pop -> to remove an element a particular index
my_list.pop()

# clear -> to empty the list
my_list.clear()

# sort -> it modifies original list
# sorted -> it doesnt modifies original list
# reverse -> reverse the list
# index -> used to find first index where element can be found
my_list.index(1)


print(my_list)