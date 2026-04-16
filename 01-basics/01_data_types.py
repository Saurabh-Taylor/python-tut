# ── Python Data Types ──────────────────────────────────────────────────────────
# Python is dynamically typed — variables don't need explicit type declarations.
# Every value has a type, which you can inspect with type() or isinstance().


# ── Primitives ─────────────────────────────────────────────────────────────────

my_int = -4
my_float = -1.5
my_string = "Hello, Saurabh!"
my_boolean = True
my_none = None  # Represents the intentional absence of a value

print(f"int     → {my_int}")
print(f"float   → {my_float}")
print(f"string  → {my_string}")
print(f"boolean → {my_boolean}")
print(f"none    → {my_none}")


# ── Collections ────────────────────────────────────────────────────────────────

# List — ordered, mutable, allows duplicates, supports mixed types
my_list = [22, "hello world", 3.14, False]
print(f"\nlist  → {my_list}")

# Tuple — ordered, immutable, allows duplicates
# Use when data should not change (e.g. coordinates, RGB values)
my_tuple = (1, 2, 3, "Hello", 4.5)
print(f"tuple → {my_tuple}  |  tuple[3] = {my_tuple[3]}")

# Set — unordered, mutable, unique elements only (duplicates are silently dropped)
my_set = {"apple", "banana", 1, 4.5, 1}     # set literal  — duplicate 1 ignored
my_set_2 = set(("saurabh", "this", "set"))  # set constructor
print(f"set   → {my_set}")
print(f"set 2 → {my_set_2}")

# Dictionary — key-value pairs; keys must be unique and hashable
my_dictionary = {
    "name": "Saurabh",
    "age": 30,
    "city": "New York",
}
print(f"dict  → {my_dictionary}")

# Range — generates a sequence of integers on demand (memory-efficient)
# Commonly used in for-loops: for i in range(5)
my_range = range(5)  # represents 0, 1, 2, 3, 4
print(f"range → {my_range}  |  as list: {list(my_range)}")


# ── Tuple vs Set (quick reference) ─────────────────────────────────────────────
# Tuple                          │ Set
# ─────────────────────────────────────────────
# Ordered (index access)         │ Unordered (no index)
# Immutable                      │ Mutable
# Allows duplicates              │ Unique elements only
# Faster iteration               │ O(1) membership test via hash table


# ── Type Inspection ────────────────────────────────────────────────────────────

# type() — returns the exact type of a value
print(f"\ntype(my_int)   → {type(my_int)}")
print(f"type(my_float) → {type(my_float)}")

# isinstance() — checks if a value is an instance of a given type (or types)
# Preferred over type() when you want to allow subclasses
print(f"isinstance('Saurabh', str) → {isinstance('Saurabh', str)}")
print(f"isinstance(1, float)       → {isinstance(1, float)}")  # False — 1 is int, not float
