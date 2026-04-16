# ── Lists ──────────────────────────────────────────────────────────────────────
# Ordered, mutable, allows duplicates, supports mixed types.
# Indexing starts at 0. Supports slicing, unpacking, and nesting.


# ── Basics: access, membership, deletion ───────────────────────────────────────

developer = ["saurabh", 23, "full stack developer", "Saurabh"]

del developer[0]                        # delete by index
print(f"after del [0]   → {developer}")

print(f"'Saurabh' in list → {'Saurabh' in developer}")  # membership check


# ── Nesting & Unpacking ────────────────────────────────────────────────────────

developer = ["Alice", 25, ["Python", "Rust", "C++"]]

print(f"nested access [2][1] → {developer[2][1]}")  # "Rust"

# Unpacking — assign list elements directly to variables
name, age, languages = developer
print(f"name={name}  age={age}  languages={languages}")

# Extended unpacking — capture remaining items with *
name, *rest = developer
print(f"name={name}  rest={rest}")


# ── Slicing ────────────────────────────────────────────────────────────────────
# Syntax: list[start:stop:step]

numbers = [1, 2, 3, 4, 5, 6]
print(f"\nnumbers           → {numbers}")
print(f"numbers[1::2]     → {numbers[1::2]}")   # every 2nd element starting at index 1


# ── Mutating Methods ───────────────────────────────────────────────────────────

my_list = [1, 2, 3, 4]
my_list_2 = [5, 6, 7]

my_list.append(my_list_2)           # adds my_list_2 as a single nested element at the end
print(f"\nafter append    → {my_list}")

my_list.insert(1, 10)               # insert value 10 at index 1
print(f"after insert    → {my_list}")

my_list.extend(my_list_2)           # adds each element of my_list_2 individually
print(f"after extend    → {my_list}")

my_list.remove(10)                  # removes the first occurrence of 10
print(f"after remove    → {my_list}")

my_list.pop()                       # removes (and returns) the last element; pop(i) removes at index i
print(f"after pop       → {my_list}")


# ── Other Useful Methods (quick reference) ─────────────────────────────────────
# sort()    — sorts in place (modifies the original list)
# sorted()  — returns a new sorted list (original unchanged)
# reverse() — reverses the list in place
# index(x)  — returns the index of the first occurrence of x
# clear()   — removes all elements from the list

my_list.clear()
print(f"after clear     → {my_list}")
