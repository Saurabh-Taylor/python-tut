# for loop

programming_languages = ['Rust', 'Java', 'Python', 'C++']

for lang in sorted(programming_languages, reverse=False):
    # print(lang)
    pass

for char in "saurabh":
    # print(char)
    pass


# for lang in programming_languages:
#     for char in "saurabh":
#         for name in "mentem":
#             print(lang, char, name)


arr = []
for i in range(3):
    for j in range(4):
        for k in range(5):
            # print(i, j, k)
            # arr.append(f'{i}, {j}, {k}')
            arr.append((i, j, k))

# print(arr[1][2])
# print(len(arr))


guess_number = 3

number = 0

# while (number != guess_number):
#     number = int(input("Enter Your Number: "))
#     if(number != guess_number):
#         print("Try Again")

# print("Yes you got it")


developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    # print(developer)



# for developer in developer_names:
#     if developer == 'Naomi':
#         break
#     print(developer)


# words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

# for word in words:
#     for letter in word:
#         if letter.lower() in 'aeiou':
#             print(f"'{word}' contains the vowel '{letter}'")
#             break
#     else:
#         print(f"'{word}' has no vowels")

# range and its use cases
# for num in range(2, 11, 2):
#     print(num)
# my_list =  list(range(2, 11, 2))
# print(my_list)


# Enumerate and Zip Functions

languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0
# one way to find the index
for lang in languages:
    index+=1

# print(dict(enumerate(languages)))


# for index, lang in enumerate(languages):
#     print(f'{type(index)} {type(lang)}')

# for index, lang in enumerate(languages, 1): # optional argument to tell where to start the index
#     print(f'{(index)} {(lang)}')


# zip functions
# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = ["is gay", 2, 3, 4]

# print(list(zip(developers, ids)))

# for name, id in zip(developers, ids):
#     print(f'Name: {name} ID: {id}')


# filter, sum, map
# lambda functions lambda a, b: a + b
