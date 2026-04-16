developer = ("saurabh", 23, "full stack developer")
developer2 = ["saurabh", 23, "full stack developer"]
my_str = "saurabh"


programming_languages = ('Python', 'Java', 'C++', 'Rust')
name, age, designation = developer
print(name, age, "full" in designation)


exists = "rust" in programming_languages
exists2 = "saurabh" in developer2
exists3 = "s" in my_str

# common methods 
# 1. count -> works with both tuples/list and if not args passed it will give error
# 2. index -> used to find the index where a particular element is present
# 3. sort and sorted -> sort modifies source iterable type but sorted returns a new list even if its tuple

a = developer2.count("saurabh")
print(a)


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3, 6))

print(len)


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
arr_list = sorted(programming_languages, key=str.lower) # so here key = len means sort based on the length
arr_list2 = sorted(programming_languages, reverse=False)
print(programming_languages)
print(arr_list)
print(arr_list2)


