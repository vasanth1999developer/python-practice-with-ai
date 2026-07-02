"""
COMPREHENSIVE COMPARISON: SETS, LISTS, TUPLES, AND DICTIONARIES
================================================================
From Basic to Advanced Level
"""

import sys
import time
from collections import defaultdict

print("=" * 90)
print("PART 1: BASIC DEFINITIONS AND CHARACTERISTICS")
print("=" * 90)

print("""
+---------------------+----------------+----------------+----------------+----------------+
|     FEATURE         |      LIST      |      TUPLE     |       SET      |   DICTIONARY   |
+---------------------+----------------+----------------+----------------+----------------+
| Definition          | Ordered        | Ordered        | Unordered      | Key-value      |
|                     | Collection     | Collection     | Collection     | Mapping        |
|                     |                |                |                |                |
| Syntax              | [1, 2, 3]      | (1, 2, 3)      | {1, 2, 3}      | {k: v, ...}    |
|                     |                |                |                |                |
| Mutability          | MUTABLE        | IMMUTABLE      | MUTABLE        | MUTABLE        |
|                     | (changeable)   | (fixed)        | (changeable)   | (changeable)   |
|                     |                |                |                |                |
| Ordered             | YES            | YES            | NO             | YES (3.7+)     |
|                     |                |                |                |                |
| Index Access        | YES (0-based)  | YES (0-based)  | NO             | NO (by key)    |
|                     |                |                |                |                |
| Allow Duplicates    | YES            | YES            | NO             | NO (keys)      |
|                     |                |                |                |                |
| Data Types          | Hetero         | Hetero         | Hetero         | Keys: Hashable |
|                     |                |                |                | Values: Any    |
|                     |                |                |                |                |
| Hashable            | NO             | YES*           | NO             | NO             |
| (dict key)          |                | (*if no list)  |                |                |
|                     |                |                |                |                |
| Performance         | Medium         | Fast           | Fast (lookup)  | Fast (lookup)  |
|                     |                |                |                |                |
| Memory              | More           | Less           | Medium         | More           |
|                     |                |                |                |                |
| Main Use            | Storing        | Immutable      | Unique         | Key-value      |
|                     | Sequences      | Sequences      | Values,        | Mapping        |
|                     |                |                | Fast Lookup    |                |
+---------------------+----------------+----------------+----------------+----------------+
""")


print("\n" + "=" * 90)
print("PART 2: CREATION METHODS")
print("=" * 90)

print("\n2.1 LIST CREATION")
print("-" * 90)
# Method 1: Direct notation
list1 = [1, 2, 3, 4]
print(f"Direct notation: {list1}")

# Method 2: Using list() constructor
list2 = list()
print(f"list() constructor: {list2}")

# Method 3: List comprehension
list3 = [x*2 for x in range(5)]
print(f"List comprehension: {list3}")

# Method 4: Nested list
list4 = [[1, 2], [3, 4], [5, 6]]
print(f"Nested list: {list4}")

print("\n2.2 TUPLE CREATION")
print("-" * 90)
# Method 1: Direct notation
tuple1 = (1, 2, 3, 4)
print(f"Direct notation: {tuple1}")

# Method 2: Without parentheses
tuple2 = 1, 2, 3, 4
print(f"Without parentheses: {tuple2}")

# Method 3: Using tuple() constructor
tuple3 = tuple([1, 2, 3, 4])
print(f"tuple() constructor: {tuple3}")

# Method 4: Single element (important!)
tuple4 = (42,)
print(f"Single element: {tuple4}")

# Method 5: Wrong - single element without comma
not_tuple = (42)
print(f"Wrong (no comma): {not_tuple} (type: {type(not_tuple).__name__})")

print("\n2.3 SET CREATION")
print("-" * 90)
# Method 1: Direct notation
set1 = {1, 2, 3, 4}
print(f"Direct notation: {set1}")

# Method 2: Using set() constructor
set2 = set([1, 2, 3, 4, 4, 4])  # Duplicates removed
print(f"set() constructor: {set2}")

# Method 3: Set comprehension
set3 = {x*2 for x in range(5)}
print(f"Set comprehension: {set3}")

# Method 4: Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")

# What {} creates
empty_dict = {}
print(f"Empty braces: {empty_dict} (type: {type(empty_dict).__name__})")

print("\n2.4 DICTIONARY CREATION")
print("-" * 90)
# Method 1: Direct notation
dict1 = {"name": "Alice", "age": 25}
print(f"Direct notation: {dict1}")

# Method 2: Using dict() constructor
dict2 = dict(name="Bob", age=30)
print(f"dict() constructor: {dict2}")

# Method 3: Dictionary comprehension
dict3 = {x: x**2 for x in range(1, 5)}
print(f"Dict comprehension: {dict3}")

# Method 4: From list of tuples
dict4 = dict([("a", 1), ("b", 2), ("c", 3)])
print(f"From list of tuples: {dict4}")

# Method 5: Using zip
keys = ["x", "y", "z"]
values = [10, 20, 30]
dict5 = dict(zip(keys, values))
print(f"Using zip: {dict5}")


print("\n" + "=" * 90)
print("PART 3: ACCESSING ELEMENTS")
print("=" * 90)

print("\n3.1 LIST ACCESS")
print("-" * 90)
my_list = [10, 20, 30, 40, 50]
print(f"List: {my_list}")
print(f"First element (index 0): {my_list[0]}")
print(f"Last element (index -1): {my_list[-1]}")
print(f"Slice [1:3]: {my_list[1:3]}")
print(f"Slice [::2]: {my_list[::2]}")

print("\n3.2 TUPLE ACCESS")
print("-" * 90)
my_tuple = (10, 20, 30, 40, 50)
print(f"Tuple: {my_tuple}")
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slice [1:3]: {my_tuple[1:3]}")

print("\n3.3 SET ACCESS")
print("-" * 90)
my_set = {10, 20, 30, 40, 50}
print(f"Set: {my_set}")
print("No index access - sets are unordered!")
print(f"Membership test (10 in set): {10 in my_set}")
print(f"Membership test (99 in set): {99 in my_set}")

print("\n3.4 DICTIONARY ACCESS")
print("-" * 90)
my_dict = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"Dictionary: {my_dict}")
print(f"Direct access: {my_dict['name']}")
print(f"Using get(): {my_dict.get('age')}")
print(f"Using get() with default: {my_dict.get('phone', 'N/A')}")


print("\n" + "=" * 90)
print("PART 4: MODIFICATION OPERATIONS")
print("=" * 90)

print("\n4.1 LIST MODIFICATIONS")
print("-" * 90)
lst = [1, 2, 3]
print(f"Original: {lst}")

lst[0] = 99  # Modify element
print(f"After lst[0] = 99: {lst}")

lst.append(4)  # Add element
print(f"After append(4): {lst}")

lst.extend([5, 6])  # Add multiple
print(f"After extend([5, 6]): {lst}")

lst.insert(0, 0)  # Insert at position
print(f"After insert(0, 0): {lst}")

lst.remove(99)  # Remove by value
print(f"After remove(99): {lst}")

print("\n4.2 TUPLE MODIFICATIONS (NOT POSSIBLE)")
print("-" * 90)
tpl = (1, 2, 3)
print(f"Original tuple: {tpl}")
try:
    tpl[0] = 99
except TypeError as e:
    print(f"Error: {e}")

print("Tuples are IMMUTABLE - Cannot be modified!")

print("\n4.3 SET MODIFICATIONS")
print("-" * 90)
s = {1, 2, 3}
print(f"Original: {s}")

s.add(4)  # Add single element
print(f"After add(4): {s}")

s.update([5, 6, 7])  # Add multiple
print(f"After update([5, 6, 7]): {s}")

s.remove(4)  # Remove element (error if not exists)
print(f"After remove(4): {s}")

s.discard(99)  # Remove if exists (no error)
print(f"After discard(99): {s}")

print("\n4.4 DICTIONARY MODIFICATIONS")
print("-" * 90)
d = {"a": 1, "b": 2}
print(f"Original: {d}")

d["c"] = 3  # Add/update
print(f"After d['c'] = 3: {d}")

d.update({"d": 4, "e": 5})
print(f"After update: {d}")

del d["a"]  # Delete
print(f"After del d['a']: {d}")


print("\n" + "=" * 90)
print("PART 5: ITERATION")
print("=" * 90)

print("\n5.1 LIST ITERATION")
print("-" * 90)
lst = ["a", "b", "c"]
print("Simple iteration:")
for item in lst:
    print(f"  {item}")

print("\nWith enumerate:")
for i, item in enumerate(lst):
    print(f"  Index {i}: {item}")

print("\n5.2 TUPLE ITERATION")
print("-" * 90)
tpl = (10, 20, 30)
print("Tuple iteration (same as list):")
for item in tpl:
    print(f"  {item}")

print("Tuple unpacking:")
x, y, z = tpl
print(f"  x={x}, y={y}, z={z}")

print("\n5.3 SET ITERATION")
print("-" * 90)
s = {3, 1, 2}
print(f"Set: {s}")
print("Iteration (no guaranteed order):")
for item in s:
    print(f"  {item}")

print("\n5.4 DICTIONARY ITERATION")
print("-" * 90)
d = {"name": "Alice", "age": 25}

print("Iterate keys:")
for key in d:
    print(f"  {key}")

print("\nIterate values:")
for value in d.values():
    print(f"  {value}")

print("\nIterate items:")
for key, value in d.items():
    print(f"  {key}: {value}")


print("\n" + "=" * 90)
print("PART 6: BUILT-IN OPERATIONS")
print("=" * 90)

print("\n6.1 LIST OPERATIONS")
print("-" * 90)
l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(f"Concatenation: {l1 + l2}")
print(f"Repetition: {l1 * 3}")
print(f"Length: {len(l1)}")
print(f"Max: {max([5, 2, 8, 1])}")
print(f"Min: {min([5, 2, 8, 1])}")
print(f"Sum: {sum([1, 2, 3, 4])}")

print("\n6.2 TUPLE OPERATIONS")
print("-" * 90)
t1 = (1, 2, 3)
t2 = (4, 5, 6)

print(f"Concatenation: {t1 + t2}")
print(f"Repetition: {t1 * 3}")
print(f"Length: {len(t1)}")
print(f"Count of 2: {t1.count(2)}")
print(f"Index of 3: {t1.index(3)}")

print("\n6.3 SET OPERATIONS")
print("-" * 90)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(f"Union (|): {s1 | s2}")
print(f"Intersection (&): {s1 & s2}")
print(f"Difference (-): {s1 - s2}")
print(f"Symmetric diff (^): {s1 ^ s2}")
print(f"Subset: {s1 <= {1, 2, 3, 4, 5}}")
print(f"Superset: {s1 >= {1, 2}}")

print("\n6.4 DICTIONARY OPERATIONS")
print("-" * 90)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

print(f"Length: {len(d1)}")
print(f"Keys: {list(d1.keys())}")
print(f"Values: {list(d1.values())}")
print(f"Merge (|): {d1 | d2}")


print("\n" + "=" * 90)
print("PART 7: PERFORMANCE COMPARISON")
print("=" * 90)

print("\n7.1 CREATION TIME")
print("-" * 90)
import timeit

# 1000 elements
list_time = timeit.timeit("x = list(range(1000))", number=100000)
tuple_time = timeit.timeit("x = tuple(range(1000))", number=100000)
set_time = timeit.timeit("x = set(range(1000))", number=100000)
dict_time = timeit.timeit("x = {i: i for i in range(1000)}", number=100000)

print(f"List creation (100k x): {list_time:.4f}s")
print(f"Tuple creation (100k x): {tuple_time:.4f}s")
print(f"Set creation (100k x): {set_time:.4f}s")
print(f"Dict creation (100k x): {dict_time:.4f}s")

print("\n7.2 LOOKUP TIME")
print("-" * 90)
setup_list = "x = list(range(10000))"
setup_set = "x = set(range(10000))"
setup_dict = "x = {i: i for i in range(10000)}"

lookup_list = timeit.timeit("5000 in x", setup=setup_list, number=100000)
lookup_set = timeit.timeit("5000 in x", setup=setup_set, number=100000)
lookup_dict = timeit.timeit("5000 in x", setup=setup_dict, number=100000)

print(f"List lookup (100k x): {lookup_list:.4f}s")
print(f"Set lookup (100k x): {lookup_set:.4f}s")
print(f"Dict lookup (100k x): {lookup_dict:.4f}s")
print("\nConclusion: Set/Dict lookup is O(1), List lookup is O(n)")

print("\n7.3 MEMORY USAGE")
print("-" * 90)
lst = list(range(100))
tpl = tuple(range(100))
s = set(range(100))
d = {i: i for i in range(100)}

print(f"List size: {sys.getsizeof(lst)} bytes")
print(f"Tuple size: {sys.getsizeof(tpl)} bytes")
print(f"Set size: {sys.getsizeof(s)} bytes")
print(f"Dict size: {sys.getsizeof(d)} bytes")


print("\n" + "=" * 90)
print("PART 8: ADVANCED COMPARISON TABLE")
print("=" * 90)

print("""
+------------------+------------------+------------------+------------------+------------------+
|     FEATURE      |       LIST       |       TUPLE      |        SET       |   DICTIONARY     |
+------------------+------------------+------------------+------------------+------------------+
| Can modify       | YES              | NO               | YES              | YES              |
| Can use as key   | NO               | YES (if hashable)| NO               | NO               |
| Preserves order  | YES              | YES              | NO               | YES (3.7+)       |
| Allows duplicates| YES              | YES              | NO               | NO (keys)        |
| Supports slicing | YES              | YES              | NO               | NO               |
| Count method     | NO               | YES              | YES              | NO               |
| Index method     | YES              | YES              | NO               | NO               |
| Add/Remove       | YES              | NO               | YES              | YES              |
| Fast lookup      | NO (O(n))        | NO (O(n))        | YES (O(1))       | YES (O(1))       |
| Mathematical ops | NO               | No               | YES (union, etc) | NO               |
| Iteration order  | Guaranteed       | Guaranteed       | Arbitrary        | Insertion order  |
| Memory efficient | Medium           | Best             | Medium           | Least            |
| Thread-safe      | NO               | YES              | NO               | NO               |
| Reversed access  | YES              | YES              | NO               | NO               |
| Sorting support  | Built-in sort()  | Can convert      | Can convert      | Can convert      |
+------------------+------------------+------------------+------------------+------------------+
""")


print("\n" + "=" * 90)
print("PART 9: WHEN TO USE EACH")
print("=" * 90)

print("""
USE LIST when:
  [+] You need to store sequences of data
  [+] You need to modify data frequently
  [+] You need to preserve order
  [+] You need to allow duplicates
  [+] You need index-based access
  [+] You need sorting/reversing
  
  Examples:
    - Shopping cart items
    - To-do list
    - Student grades
    - Game scores

USE TUPLE when:
  [+] You need immutable data (safety)
  [+] You need hashable data (dict keys, set elements)
  [+] You're returning multiple values from function
  [+] You need to protect data from changes
  [+] You need slight performance advantage
  [+] You're using it as a key
  
  Examples:
    - Coordinate pairs (x, y)
    - RGB color values (255, 128, 64)
    - Function return values
    - Dictionary keys
    - Set elements

USE SET when:
  [+] You need unique values only
  [+] You need fast membership testing
  [+] You need mathematical operations (union, intersection)
  [+] You need to remove duplicates
  [+] You need to find common elements
  [+] You don't care about order
  
  Examples:
    - Unique user IDs
    - Finding common friends
    - Removing duplicates from list
    - Checking membership
    - Finding unique tags

USE DICTIONARY when:
  [+] You need key-value mapping
  [+] You need fast lookup by key
  [+] You need labeled data
  [+] You're counting occurrences
  [+] You need nested data structures
  [+] You need to preserve insertion order
  
  Examples:
    - User profiles
    - Configuration settings
    - Counting word frequency
    - Mapping IDs to names
    - Nested data (JSON-like)
""")


print("\n" + "=" * 90)
print("PART 10: CONVERSION BETWEEN DATA STRUCTURES")
print("=" * 90)

original_list = [1, 2, 3, 4, 5]

print(f"Original list: {original_list}")
print(f"List to tuple: {tuple(original_list)}")
print(f"List to set: {set(original_list)}")
print(f"List to dict (with enum): {dict(enumerate(original_list))}")

print("\n---")

original_tuple = (1, 2, 3, 4, 5)
print(f"Original tuple: {original_tuple}")
print(f"Tuple to list: {list(original_tuple)}")
print(f"Tuple to set: {set(original_tuple)}")

print("\n---")

original_set = {1, 2, 3, 4, 5}
print(f"Original set: {original_set}")
print(f"Set to list: {list(original_set)}")
print(f"Set to tuple: {tuple(original_set)}")

print("\n---")

original_dict = {"a": 1, "b": 2, "c": 3}
print(f"Original dict: {original_dict}")
print(f"Dict keys to list: {list(original_dict.keys())}")
print(f"Dict values to list: {list(original_dict.values())}")
print(f"Dict items to list: {list(original_dict.items())}")
print(f"Dict items to tuple: {tuple(original_dict.items())}")


print("\n" + "=" * 90)
print("PART 11: PRACTICAL EXAMPLES")
print("=" * 90)

print("\n11.1 EXAMPLE: Remove Duplicates from List")
print("-" * 90)
scores = [90, 85, 90, 92, 85, 88, 92, 90]
print(f"Original scores: {scores}")
print(f"Duplicates removed: {list(set(scores))}")
print(f"Sorted unique: {sorted(set(scores))}")

print("\n11.2 EXAMPLE: Find Common Elements")
print("-" * 90)
friends_alice = {"Bob", "Charlie", "David", "Eve"}
friends_bob = {"Alice", "Charlie", "Frank", "David"}
print(f"Alice's friends: {friends_alice}")
print(f"Bob's friends: {friends_bob}")
print(f"Common friends: {friends_alice & friends_bob}")

print("\n11.3 EXAMPLE: Store User Information")
print("-" * 90)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]
print("User database (List of Dicts):")
for user in users:
    print(f"  {user['name']} ({user['email']})")

print("\n11.4 EXAMPLE: Track Visited Websites")
print("-" * 90)
visited = set()
websites = ["google.com", "github.com", "google.com", "python.org", "github.com"]
for site in websites:
    visited.add(site)
print(f"Websites visited: {len(visited)}")
print(f"Unique sites: {visited}")

print("\n11.5 EXAMPLE: Store Coordinates")
print("-" * 90)
# Tuples for coordinates (immutable, hashable)
waypoints = ((0, 0), (10, 20), (30, 40), (50, 60))
print(f"Route waypoints: {waypoints}")
print(f"First waypoint: {waypoints[0]}")
print(f"Last waypoint: {waypoints[-1]}")

# Using coordinates as dictionary keys
location_names = {
    (0, 0): "Start",
    (10, 20): "Checkpoint 1",
    (50, 60): "Finish"
}
print(f"Location map: {location_names}")
print(f"Point (0, 0): {location_names[(0, 0)]}")


print("\n" + "=" * 90)
print("PART 12: NESTED STRUCTURES")
print("=" * 90)

print("\n12.1 COMPLEX NESTED EXAMPLE")
print("-" * 90)

school_data = {
    "school": "Tech Academy",
    "students": [
        {
            "name": "Alice",
            "id": 101,
            "grades": (90, 85, 92),  # Tuple for immutable grades
            "tags": {"honors", "athlete"}  # Set for unique tags
        },
        {
            "name": "Bob",
            "id": 102,
            "grades": (78, 82, 80),
            "tags": {"tech-club"}
        }
    ],
    "courses": {
        "CS101": ["Alice", "Bob", "Charlie"],
        "MATH101": ["Alice", "David"]
    }
}

print("School data structure:")
print(f"School: {school_data['school']}")
print(f"First student: {school_data['students'][0]['name']}")
print(f"First student grades: {school_data['students'][0]['grades']}")
print(f"First student tags: {school_data['students'][0]['tags']}")
print(f"CS101 students: {school_data['courses']['CS101']}")


print("\n" + "=" * 90)
print("PART 13: DECISION TREE")
print("=" * 90)

print("""
Choose your data structure:

1. Do you need key-value pairs?
   YES  -> Use DICTIONARY
   NO   -> Continue to 2

2. Do you need to modify the collection after creation?
   YES  -> Continue to 3
   NO   -> Use TUPLE (immutable, hashable, fast)

3. Do you need unique values only?
   YES  -> Use SET (fast lookups, mathematical ops)
   NO   -> Use LIST (ordered, indexed, flexible)

DECISION EXAMPLES:

Task: Store student names in order
  -> LIST (ordered, mutable)

Task: Return multiple values from function
  -> TUPLE (immutable, hashable)

Task: Check if user is in allowed list
  -> SET (O(1) lookup time)

Task: Store configuration settings
  -> DICTIONARY (key-value mapping)

Task: Store coordinates for a point
  -> TUPLE (immutable, can use as key)

Task: Store shopping cart items
  -> LIST (can add/remove, preserve order)

Task: Find unique colors in image
  -> SET (remove duplicates, fast)

Task: Map employee IDs to names
  -> DICTIONARY (key-value mapping)
""")


print("\n" + "=" * 90)
print("PART 14: COMMON MISTAKES")
print("=" * 90)

print("""
MISTAKE 1: Using {} for empty set
  WRONG: empty = {}          # This creates a dict!
  RIGHT: empty = set()       # This creates a set

MISTAKE 2: Single element tuple without comma
  WRONG: tpl = (42)          # This is an int!
  RIGHT: tpl = (42,)         # This is a tuple

MISTAKE 3: Trying to modify tuple
  WRONG: tpl = (1, 2, 3)
         tpl[0] = 99        # TypeError!
  RIGHT: lst = [1, 2, 3]
         lst[0] = 99        # Works fine

MISTAKE 4: Using list as dictionary key
  WRONG: d = {[1, 2]: "value"}  # TypeError!
  RIGHT: d = {(1, 2): "value"}  # Tuples work

MISTAKE 5: Expecting order in sets
  WRONG: s = {1, 2, 3}
         print(s)  # May print in any order
  RIGHT: if order matters, use list or tuple

MISTAKE 6: Shallow copy confusion
  WRONG: dict_copy = dict1  # Refers to same dict
  RIGHT: dict_copy = dict1.copy()  # Creates new dict

MISTAKE 7: Set duplicates surprise
  WRONG: s = {1, 1, 1, 2, 2, 3}  # Duplicates ignored
  RIGHT: Use this feature intentionally
""")


print("\n" + "=" * 90)
print("PART 15: SUMMARY COMPARISON TABLE")
print("=" * 90)

print("""
QUICK REFERENCE GUIDE
=====================

DATA TYPE      SYNTAX        MUTABLE  ORDERED  UNIQUE  HASHABLE  USE FOR
---            ------        -------  -------  ------  --------  -------
List           [1,2,3]       YES      YES      NO      NO        Sequences
Tuple          (1,2,3)       NO       YES      NO      YES*      Immutable data
Set            {1,2,3}       YES      NO       YES     NO        Unique values
Dictionary     {k:v}         YES      YES**    Keys    NO        Key-value pairs

* Tuple is hashable only if it contains no mutable elements
** As of Python 3.7+

PERFORMANCE COMPARISON (for 10,000 elements)
=============================================

Operation            List      Tuple     Set       Dict
---------            ----      -----     ---       ----
Creation             Medium    Fast      Fast      Fast
Lookup               Slow O(n) Slow O(n) Fast O(1) Fast O(1)
Insertion            Medium    N/A       Medium    Medium
Deletion             Medium    N/A       Medium    Medium
Memory               More      Less      Medium    More

BEST PRACTICES
==============

1. Use LISTS for ordered, mutable sequences
2. Use TUPLES for immutable, hashable data
3. Use SETS for unique values and fast lookups
4. Use DICTS for key-value mappings
5. Use SETS for checking membership (not lists)
6. Use TUPLES as dictionary keys (not lists)
7. Comprehensions work with all four types
8. Convert between types using constructors
9. Choose based on your specific needs
10. Profile your code for performance-critical sections
""")

print("\n" + "=" * 90)
print("END OF COMPREHENSIVE COMPARISON")
print("=" * 90)
