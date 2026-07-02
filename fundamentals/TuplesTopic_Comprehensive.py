"""
COMPREHENSIVE GUIDE TO TUPLES AND TUPLE VS LIST COMPARISON
===========================================================
"""

import sys
from typing import Tuple

print("=" * 80)
print("PART 1: DETAILED DEFINITION OF TUPLES")
print("=" * 80)

print("""
DEFINITION OF TUPLE:
====================
A tuple is an IMMUTABLE, ORDERED collection of elements in Python.

Key Characteristics:
1. IMMUTABLE - Cannot be modified after creation (no add, remove, change)
2. ORDERED - Elements maintain their position/index
3. HETEROGENEOUS - Can contain elements of different data types
4. INDEXED - Each element has a position (0-based indexing)
5. ITERABLE - Can be looped over
6. ALLOW DUPLICATES - Same element can appear multiple times
7. LIGHTWEIGHT - More memory efficient than lists
""")

print("\n" + "=" * 80)
print("PART 2: CREATING TUPLES")
print("=" * 80)

# 2.1 Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")
print(f"Type: {type(empty_tuple)}")

# 2.2 Single element tuple (note the comma)
single_element = (42,)
print(f"\nSingle element tuple: {single_element}")
print(f"Type: {type(single_element)}")

# Without comma, it's just a value in parentheses
not_a_tuple = (42)
print(f"Not a tuple (no comma): {not_a_tuple}")
print(f"Type: {type(not_a_tuple)}")

# 2.3 Multiple elements
colors = ("red", "green", "blue")
print(f"\nTuple with multiple elements: {colors}")

# 2.4 Mixed data types
mixed = (1, "hello", 3.14, True, None)
print(f"Mixed data types: {mixed}")

# 2.5 Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuples: {nested}")

# 2.6 Without parentheses (Python unpacking)
tuple_unpacking = 10, 20, 30
print(f"Tuple without parentheses: {tuple_unpacking}")

# 2.7 Using tuple() constructor
list_to_tuple = tuple([1, 2, 3, 4, 5])
print(f"Created from list: {list_to_tuple}")

# 2.8 From string
string_to_tuple = tuple("hello")
print(f"Created from string: {string_to_tuple}")


print("\n" + "=" * 80)
print("PART 3: ACCESSING TUPLE ELEMENTS")
print("=" * 80)

student = ("Alice", "Engineering", 3.8, 2023)

# 3.1 Positive indexing
print(f"First element (index 0): {student[0]}")
print(f"Second element (index 1): {student[1]}")
print(f"Third element (index 2): {student[2]}")

# 3.2 Negative indexing
print(f"\nLast element (index -1): {student[-1]}")
print(f"Second last element (index -2): {student[-2]}")

# 3.3 Slicing
print(f"\nSlice [0:2]: {student[0:2]}")
print(f"Slice [1:3]: {student[1:3]}")
print(f"Slice [::2]: {student[::2]}")
print(f"Slice [::-1] (reverse): {student[::-1]}")


print("\n" + "=" * 80)
print("PART 4: TUPLE METHODS")
print("=" * 80)

numbers = (1, 2, 3, 4, 5, 2, 2, 3)

# 4.1 count() - count occurrences
print(f"Tuple: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Count of 5: {numbers.count(5)}")
print(f"Count of 10: {numbers.count(10)}")

# 4.2 index() - find first index
print(f"\nIndex of 2: {numbers.index(2)}")
print(f"Index of 4: {numbers.index(4)}")

# 4.3 Length
print(f"\nLength: {len(numbers)}")

# 4.4 Membership test
print(f"\nIs 3 in tuple: {3 in numbers}")
print(f"Is 99 in tuple: {99 in numbers}")


print("\n" + "=" * 80)
print("PART 5: TUPLE UNPACKING")
print("=" * 80)

# 5.1 Simple unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: {coordinates}")
print(f"x = {x}, y = {y}")

# 5.2 Unpacking with multiple values
person = ("John", 25, "Engineer")
name, age, job = person
print(f"\nName: {name}, Age: {age}, Job: {job}")

# 5.3 Extended unpacking with *
values = (1, 2, 3, 4, 5)
first, *middle, last = values
print(f"\nFirst: {first}, Middle: {middle}, Last: {last}")

# 5.4 Ignoring values with _
rgb = (255, 128, 64)
r, _, b = rgb
print(f"Red: {r}, Blue: {b} (ignored green)")


print("\n" + "=" * 80)
print("PART 6: TUPLE IMMUTABILITY")
print("=" * 80)

original = (1, 2, 3)
print(f"Original tuple: {original}")

# 6.1 Cannot modify elements
try:
    original[0] = 99
except TypeError as e:
    print(f"Cannot modify: {e}")

# 6.2 Cannot add elements
try:
    original.append(4)
except AttributeError as e:
    print(f"Cannot append: {e}")

# 6.3 Cannot delete elements
try:
    del original[0]
except TypeError as e:
    print(f"Cannot delete: {e}")

# 6.4 Creating new tuple by concatenation
print(f"\nOriginal: {original}")
new_tuple = original + (4, 5)
print(f"After concatenation: {new_tuple}")
print(f"Original unchanged: {original}")


print("\n" + "=" * 80)
print("PART 7: TUPLE OPERATIONS")
print("=" * 80)

# 7.1 Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Concatenation: {tuple1} + {tuple2} = {combined}")

# 7.2 Repetition
repeated = (1, 2) * 3
print(f"Repetition: (1, 2) * 3 = {repeated}")

# 7.3 Iteration
print(f"\nIteration over ('a', 'b', 'c'):")
for item in ('a', 'b', 'c'):
    print(f"  {item}")

# 7.4 Min, Max, Sum
numbers_tuple = (5, 2, 8, 1, 9)
print(f"\nTuple: {numbers_tuple}")
print(f"Min: {min(numbers_tuple)}")
print(f"Max: {max(numbers_tuple)}")
print(f"Sum: {sum(numbers_tuple)}")

# 7.5 Sorting (creates list)
sorted_tuple = tuple(sorted(numbers_tuple))
print(f"Sorted: {sorted_tuple}")


print("\n" + "=" * 80)
print("PART 8: TUPLE VS LIST - COMPREHENSIVE COMPARISON")
print("=" * 80)

print("""
+==========================+============================+=======================+
|      FEATURE             |        TUPLE               |         LIST           |
+==========================+============================+=======================+
| Syntax                   | (1, 2, 3)                  | [1, 2, 3]             |
| Mutability               | IMMUTABLE                  | MUTABLE               |
| Ordered                  | YES                        | YES                   |
| Index Access             | YES (0-based)              | YES (0-based)         |
| Allow Duplicates         | YES                        | YES                   |
| Data Types               | Heterogeneous              | Heterogeneous         |
| Hashable                 | YES (if no mutables)       | NO                    |
| Performance              | FASTER, Less Memory        | SLOWER, More Memory   |
| Use as Dict Key          | YES                        | NO                    |
| Thread-Safe              | YES (Immutable)            | NO                    |
+==========================+============================+=======================+
""")

print("\n" + "=" * 80)
print("PART 9: DETAILED COMPARISON WITH EXAMPLES")
print("=" * 80)

print("\n9.1 MUTABILITY - The Main Difference")
print("-" * 80)

# List - Mutable
print("LIST (Mutable) - Can be changed:")
my_list = [1, 2, 3]
print(f"  Original list: {my_list}")
my_list[0] = 99
print(f"  After my_list[0] = 99: {my_list}")
my_list.append(4)
print(f"  After my_list.append(4): {my_list}")

# Tuple - Immutable
print("\nTUPLE (Immutable) - Cannot be changed:")
my_tuple = (1, 2, 3)
print(f"  Original tuple: {my_tuple}")
try:
    my_tuple[0] = 99
except TypeError:
    print(f"  Cannot modify: my_tuple[0] = 99 raises TypeError")


print("\n9.2 PERFORMANCE COMPARISON")
print("-" * 80)

# Creating and accessing
import timeit

setup_list = "my_list = list(range(1000))"
setup_tuple = "my_tuple = tuple(range(1000))"

# Creation time
list_time = timeit.timeit("list(range(1000))", number=100000)
tuple_time = timeit.timeit("tuple(range(1000))", number=100000)
print(f"Creation time for 1000 elements (100k iterations):")
print(f"  List:  {list_time:.4f} seconds")
print(f"  Tuple: {tuple_time:.4f} seconds")
print(f"  Tuple is {list_time/tuple_time:.2f}x faster")

# Iteration time
list_iter = timeit.timeit("for x in my_list: pass", setup=setup_list, number=100000)
tuple_iter = timeit.timeit("for x in my_tuple: pass", setup=setup_tuple, number=100000)
print(f"\nIteration time for 1000 elements (100k iterations):")
print(f"  List:  {list_iter:.4f} seconds")
print(f"  Tuple: {tuple_iter:.4f} seconds")

# Memory usage
list_obj = list(range(100))
tuple_obj = tuple(range(100))
print(f"\nMemory usage for 100 elements:")
print(f"  List size:  {sys.getsizeof(list_obj)} bytes")
print(f"  Tuple size: {sys.getsizeof(tuple_obj)} bytes")
print(f"  Tuple uses {sys.getsizeof(list_obj) - sys.getsizeof(tuple_obj)} bytes less")


print("\n9.3 HASHABILITY - Tuple as Dictionary Key")
print("-" * 80)

# Can use tuple as dictionary key
location_data = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago",
}
print("Dictionary with tuple keys (coordinates):")
for coord, city in location_data.items():
    print(f"  {coord} -> {city}")

# Cannot use list as dictionary key
print("\nUsing list as dictionary key:")
try:
    bad_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"  Error: {e}")


print("\n9.4 THREAD SAFETY - Tuples are Thread-Safe")
print("-" * 80)

print("""
Tuple (Thread-Safe):
  - Immutable, so no race conditions
  - Safe to share between threads without locks
  - Multiple threads can read simultaneously

List (NOT Thread-Safe):
  - Mutable operations can cause race conditions
  - Needs synchronization (locks) for multi-threaded access
  - Concurrent modifications can corrupt data
""")


print("\n9.5 BUILT-IN METHODS COMPARISON")
print("-" * 80)

print("\nLIST Methods (Mutating operations):")
print("  - append()      : Add single element")
print("  - extend()      : Add multiple elements")
print("  - insert()      : Insert at position")
print("  - remove()      : Remove by value")
print("  - pop()         : Remove and return element")
print("  - clear()       : Remove all elements")
print("  - sort()        : Sort in-place")
print("  - reverse()     : Reverse in-place")

print("\nTUPLE Methods (Non-mutating operations):")
print("  - count()       : Count occurrences")
print("  - index()       : Find first index")
print("  (That's it! No mutation methods)")


print("\n9.6 WHEN TO USE TUPLE vs LIST")
print("-" * 80)

print("""
USE TUPLE when:
  [OK] Data should not be modified (safety)
  [OK] Need to use as dictionary key
  [OK] Function returns multiple values
  [OK] Want thread-safe collection
  [OK] Need better performance (faster, less memory)
  [OK] Preventing accidental modifications
  [OK] Need hashable collection
  [OK] Working with function arguments/returns

USE LIST when:
  [OK] Need to add/remove/modify elements
  [OK] Don't need key-value association
  [OK] Order may change dynamically
  [OK] Need sorting/reversing in-place
  [OK] Want rich set of methods
  [OK] Building dynamic collections
""")


print("\n" + "=" * 80)
print("PART 10: PRACTICAL EXAMPLES")
print("=" * 80)

print("\n10.1 Example 1: Function Returns Multiple Values (Using Tuple)")
print("-" * 80)

def get_min_max(numbers):
    """Return both min and max as tuple"""
    return (min(numbers), max(numbers))

data = [5, 2, 8, 1, 9, 3]
min_val, max_val = get_min_max(data)
print(f"Data: {data}")
print(f"Min: {min_val}, Max: {max_val}")


print("\n10.2 Example 2: Storing Immutable Data (Using Tuple)")
print("-" * 80)

# Configuration - should not change
CONFIG = {
    "database": ("localhost", 5432, "production"),
    "cache": ("redis-server", 6379),
    "security": ("TLS 1.2", "SHA-256"),
}

for key, value in CONFIG.items():
    print(f"{key}: {value}")

print("\nNote: CONFIG values are protected from accidental modification")


print("\n10.3 Example 3: Student Records Using Tuple")
print("-" * 80)

students = [
    ("Alice", 101, 3.8),
    ("Bob", 102, 3.5),
    ("Charlie", 103, 3.9),
    ("David", 104, 3.2),
]

print("Student Records (name, ID, GPA):")
for name, student_id, gpa in students:
    status = "Honor Roll" if gpa >= 3.7 else "Good Standing"
    print(f"  {name} (ID: {student_id}) - GPA: {gpa} - {status}")


print("\n10.4 Example 4: Coordinates and Locations (Using Tuple)")
print("-" * 80)

locations = {
    (28.6139, 77.2090): "New Delhi, India",
    (40.7128, -74.0060): "New York, USA",
    (51.5074, -0.1278): "London, UK",
    (35.6762, 139.6503): "Tokyo, Japan",
}

print("Coordinates -> City:")
for (lat, lon), city in locations.items():
    print(f"  ({lat}, {lon}) -> {city}")


print("\n10.5 Example 5: Dynamic Collection (Using List)")
print("-" * 80)

shopping_cart = []
items = [("Apple", 5), ("Banana", 3), ("Milk", 2)]

print("Adding items to cart:")
for item, quantity in items:
    shopping_cart.append((item, quantity))
    print(f"  Added {quantity}x {item}")

print(f"\nCart: {shopping_cart}")

# Modify cart
shopping_cart[0] = ("Mango", 4)
print(f"After changing first item: {shopping_cart}")

shopping_cart.append(("Orange", 6))
print(f"After adding Orange: {shopping_cart}")


print("\n10.6 Example 6: Mixed Usage in a Program")
print("-" * 80)

class Library:
    def __init__(self):
        self.catalog = {}
    
    def add_book(self, title, author, isbn):
        # Using tuple as key (immutable, hashable)
        key = (title, author)
        self.catalog[key] = isbn
    
    def get_book_info(self, title, author):
        # Return tuple with multiple values
        if (title, author) in self.catalog:
            return (title, author, self.catalog[(title, author)])
        return None
    
    def list_books(self):
        # Return list of tuples (mutable collection of immutable items)
        return list(self.catalog.items())

lib = Library()
lib.add_book("1984", "George Orwell", "978-0451524935")
lib.add_book("Brave New World", "Aldous Huxley", "978-0060085239")
lib.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")

print("Books in library:")
for book_key, isbn in lib.list_books():
    print(f"  {book_key[0]} by {book_key[1]} (ISBN: {isbn})")

info = lib.get_book_info("1984", "George Orwell")
if info:
    print(f"\nFound: {info[0]} by {info[1]} (ISBN: {info[2]})")


print("\n" + "=" * 80)
print("PART 11: SUMMARY TABLE")
print("=" * 80)

print("""
+==========================+============================+=======================+
|      FEATURE             |        TUPLE               |         LIST           |
+==========================+============================+=======================+
| Syntax                   | (1, 2, 3)                  | [1, 2, 3]             |
| Mutability               | IMMUTABLE                  | MUTABLE               |
| Ordered                  | YES                        | YES                   |
| Index Access             | YES (0-based)              | YES (0-based)         |
| Allow Duplicates         | YES                        | YES                   |
| Data Types               | Heterogeneous              | Heterogeneous         |
| Hashable                 | YES (if no mutables)       | NO                    |
| Performance              | FASTER, Less Memory        | SLOWER, More Memory   |
| Use as Dict Key          | YES                        | NO                    |
| Thread-Safe              | YES (Immutable)            | NO                    |
+==========================+============================+=======================+
""")

print("\n" + "=" * 80)
print("END OF COMPREHENSIVE TUPLE GUIDE")
print("=" * 80)
