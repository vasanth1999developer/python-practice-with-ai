"""
COMPREHENSIVE GUIDE TO PYTHON DICTIONARIES
============================================
All topics, methods, operations, and advanced techniques
"""

print("=" * 80)
print("PART 1: INTRODUCTION TO DICTIONARIES")
print("=" * 80)

print("""
DEFINITION:
===========
A dictionary is a MUTABLE, UNORDERED collection of KEY-VALUE pairs in Python.
(As of Python 3.7+, dictionaries maintain insertion order)

Key Characteristics:
1. MUTABLE - Can be modified (add, remove, update)
2. ORDERED - Maintains insertion order (Python 3.7+)
3. INDEXED by KEYS - Access values using keys (not integers)
4. KEY-VALUE PAIRS - Each key maps to one value
5. UNIQUE KEYS - Keys must be unique and hashable
6. HETEROGENEOUS - Keys and values can be any type
7. UNINDEXED - No numeric indexing, uses keys instead
""")


print("\n" + "=" * 80)
print("PART 2: CREATING DICTIONARIES")
print("=" * 80)

# 2.1 Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")
print(f"Type: {type(empty_dict)}")

# 2.2 Using dict() constructor
empty_dict2 = dict()
print(f"Empty dict using dict(): {empty_dict2}")

# 2.3 Dictionary with initial values
student = {
    "name": "Alice",
    "age": 20,
    "gpa": 3.8,
    "major": "Computer Science"
}
print(f"\nStudent dictionary: {student}")

# 2.4 Mixed keys and values
mixed = {
    1: "one",
    "two": 2,
    3.14: "pi",
    (1, 2): "tuple_key",
    True: "boolean"
}
print(f"Mixed types: {mixed}")

# 2.5 Nested dictionary
company = {
    "name": "TechCorp",
    "employees": {
        "emp1": {"name": "John", "dept": "IT"},
        "emp2": {"name": "Jane", "dept": "HR"}
    },
    "location": "New York"
}
print(f"Nested dictionary: {company}")

# 2.6 Using dict() constructor with key-value pairs
from_dict = dict(name="Bob", age=25, city="London")
print(f"Created with dict(): {from_dict}")

# 2.7 Using zip() to create dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
zipped = dict(zip(keys, values))
print(f"From zip: {zipped}")

# 2.8 Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Dictionary comprehension: {squares}")


print("\n" + "=" * 80)
print("PART 3: ACCESSING DICTIONARY VALUES")
print("=" * 80)

person = {"name": "Charlie", "age": 30, "city": "Boston"}

# 3.1 Using key
print(f"person['name']: {person['name']}")
print(f"person['age']: {person['age']}")

# 3.2 Using get() method
print(f"\nUsing get(): {person.get('city')}")
print(f"Using get() with default: {person.get('phone', 'N/A')}")

# 3.3 Checking if key exists
print(f"\n'name' in person: {'name' in person}")
print(f"'phone' in person: {'phone' in person}")

# 3.4 Accessing keys and values
print(f"\nAll keys: {person.keys()}")
print(f"All values: {person.values()}")
print(f"All items (key-value pairs): {person.items()}")


print("\n" + "=" * 80)
print("PART 4: ADDING, UPDATING, AND REMOVING")
print("=" * 80)

data = {"a": 1, "b": 2}
print(f"Original: {data}")

# 4.1 Adding new key-value
data["c"] = 3
print(f"After adding 'c': {data}")

# 4.2 Updating existing key
data["a"] = 10
print(f"After updating 'a': {data}")

# 4.3 Using update() method
data.update({"d": 4, "e": 5})
print(f"After update(): {data}")

# 4.4 Removing by key using del
del data["b"]
print(f"After del data['b']: {data}")

# 4.5 Using pop() method
value = data.pop("c")
print(f"Popped 'c' (value: {value}): {data}")

# 4.6 Using popitem() - removes last item
last_item = data.popitem()
print(f"Popped last item {last_item}: {data}")

# 4.7 Using clear()
temp = {"x": 1, "y": 2}
temp.clear()
print(f"After clear(): {temp}")

# 4.8 Using setdefault()
data.setdefault("new_key", "new_value")
print(f"After setdefault(): {data}")


print("\n" + "=" * 80)
print("PART 5: DICTIONARY METHODS")
print("=" * 80)

d = {"apple": 5, "banana": 3, "orange": 7}

# 5.1 keys()
print(f"keys(): {list(d.keys())}")

# 5.2 values()
print(f"values(): {list(d.values())}")

# 5.3 items()
print(f"items(): {list(d.items())}")

# 5.4 get()
print(f"get('apple'): {d.get('apple')}")
print(f"get('grape', 0): {d.get('grape', 0)}")

# 5.5 pop()
print(f"pop('banana'): {d.pop('banana')}")
print(f"Dictionary after pop: {d}")

# 5.6 popitem()
d = {"a": 1, "b": 2, "c": 3}
print(f"popitem(): {d.popitem()}")

# 5.7 update()
d.update({"d": 4, "e": 5})
print(f"After update: {d}")

# 5.8 clear()
temp = {"x": 1}
temp.clear()
print(f"After clear: {temp}")

# 5.9 copy()
original = {"key": "value"}
copy_dict = original.copy()
copy_dict["key"] = "new_value"
print(f"Original: {original}, Copy: {copy_dict}")

# 5.10 setdefault()
d = {"name": "Alice"}
d.setdefault("age", 25)
print(f"After setdefault: {d}")


print("\n" + "=" * 80)
print("PART 6: ITERATION")
print("=" * 80)

scores = {"Alice": 90, "Bob": 85, "Charlie": 95}

# 6.1 Iterate over keys
print("Iterating over keys:")
for key in scores:
    print(f"  {key}")

# 6.2 Iterate over values
print("\nIterating over values:")
for value in scores.values():
    print(f"  {value}")

# 6.3 Iterate over items
print("\nIterating over items:")
for key, value in scores.items():
    print(f"  {key}: {value}")

# 6.4 Iterate with enumerate
print("\nIterating with enumerate:")
for i, (key, value) in enumerate(scores.items(), 1):
    print(f"  {i}. {key}: {value}")


print("\n" + "=" * 80)
print("PART 7: DICTIONARY COMPREHENSION")
print("=" * 80)

# 7.1 Basic comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# 7.2 With condition
evens = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {evens}")

# 7.3 From list
items = ["apple", "banana", "orange"]
lengths = {item: len(item) for item in items}
print(f"String lengths: {lengths}")

# 7.4 From existing dict
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v*2 for k, v in original.items()}
print(f"Doubled values: {doubled}")

# 7.5 Swap keys and values
mapping = {"x": 1, "y": 2, "z": 3}
swapped = {v: k for k, v in mapping.items()}
print(f"Swapped: {swapped}")


print("\n" + "=" * 80)
print("PART 8: NESTED DICTIONARIES")
print("=" * 80)

# 8.1 Accessing nested values
employees = {
    "emp001": {"name": "John", "age": 30, "skills": ["Python", "SQL"]},
    "emp002": {"name": "Jane", "age": 28, "skills": ["Java", "C++"]}
}

print(f"First employee name: {employees['emp001']['name']}")
print(f"First employee skills: {employees['emp001']['skills']}")

# 8.2 Modifying nested values
employees["emp001"]["age"] = 31
print(f"Updated age: {employees['emp001']['age']}")

# 8.3 Adding to nested dict
employees["emp001"]["salary"] = 75000
print(f"After adding salary: {employees['emp001']}")

# 8.4 Iterating nested dict
print("\nAll employees:")
for emp_id, emp_data in employees.items():
    print(f"  {emp_id}: {emp_data['name']} (Age: {emp_data['age']})")


print("\n" + "=" * 80)
print("PART 9: MERGING DICTIONARIES")
print("=" * 80)

# 9.1 Using update()
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(f"After update: {dict1}")

# 9.2 Using ** (unpacking) - Python 3.5+
d1 = {"x": 1, "y": 2}
d2 = {"z": 3, "w": 4}
merged = {**d1, **d2}
print(f"Unpacking merge: {merged}")

# 9.3 Using | operator - Python 3.9+
d3 = {"a": 1, "b": 2}
d4 = {"c": 3, "d": 4}
merged2 = d3 | d4
print(f"Using |: {merged2}")

# 9.4 Using dict() constructor
dict_a = {"p": 1}
dict_b = {"q": 2}
combined = dict(dict_a, **dict_b)
print(f"Using dict(): {combined}")


print("\n" + "=" * 80)
print("PART 10: DICTIONARY VS OTHER DATA STRUCTURES")
print("=" * 80)

print("""
DICTIONARY vs LIST:
  Dictionary: Key-value pairs, unindexed by position
  List: Indexed by position (0, 1, 2, ...)
  
  Example:
  person = {"name": "Alice", "age": 30}  # Access by key
  items = [1, 2, 3]  # Access by index

DICTIONARY vs SET:
  Dictionary: Has keys and values
  Set: Only unique values, no keys
  
  Example:
  mapping = {"a": 1, "b": 2}  # Key-value
  unique = {1, 2, 3}  # Values only

DICTIONARY vs TUPLE:
  Dictionary: Mutable, unordered (until 3.7), keyed
  Tuple: Immutable, ordered, indexed
  
  Example:
  config = {"host": "localhost", "port": 5432}  # Dict
  point = (10, 20)  # Tuple
""")


print("\n" + "=" * 80)
print("PART 11: ADVANCED TECHNIQUES")
print("=" * 80)

# 11.1 Default values using defaultdict
from collections import defaultdict

print("11.1 defaultdict - Auto-create missing keys:")
count = defaultdict(int)
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    count[word] += 1
print(f"Word count: {dict(count)}")

# 11.2 OrderedDict (for older Python versions)
from collections import OrderedDict
print("\n11.2 OrderedDict - Maintains order explicitly:")
ordered = OrderedDict([("z", 1), ("a", 2), ("m", 3)])
print(f"Ordered dict: {ordered}")

# 11.3 Counter - Count occurrences
from collections import Counter
print("\n11.3 Counter - Count elements:")
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(items)
print(f"Counter: {dict(counter)}")
print(f"Most common 2: {counter.most_common(2)}")

# 11.4 ChainMap - Combine multiple dicts
from collections import ChainMap
print("\n11.4 ChainMap - View multiple dicts as one:")
config_default = {"host": "localhost", "port": 8000}
config_override = {"port": 9000}
chain = ChainMap(config_override, config_default)
print(f"ChainMap: {dict(chain)}")

# 11.5 Shallow vs Deep copy
print("\n11.5 Shallow vs Deep copy:")
import copy
original = {"a": [1, 2, 3], "b": {"x": 10}}
shallow = original.copy()
deep = copy.deepcopy(original)

shallow["a"][0] = 99
deep["b"]["x"] = 99

print(f"Original: {original}")
print(f"Shallow (affected): {shallow}")
print(f"Deep (not affected): {deep}")


print("\n" + "=" * 80)
print("PART 12: SORTING DICTIONARIES")
print("=" * 80)

data = {"banana": 3, "apple": 5, "orange": 2, "grape": 4}

# 12.1 Sort by keys
sorted_by_keys = dict(sorted(data.items()))
print(f"Sorted by keys: {sorted_by_keys}")

# 12.2 Sort by values
sorted_by_values = dict(sorted(data.items(), key=lambda x: x[1]))
print(f"Sorted by values: {sorted_by_values}")

# 12.3 Sort in reverse
sorted_reverse = dict(sorted(data.items(), reverse=True))
print(f"Sorted reverse: {sorted_reverse}")

# 12.4 Sort by custom key
students = {"Alice": 90, "Bob": 85, "Charlie": 95}
top_to_bottom = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
print(f"Top to bottom (scores): {top_to_bottom}")


print("\n" + "=" * 80)
print("PART 13: FILTERING DICTIONARIES")
print("=" * 80)

scores = {"Alice": 90, "Bob": 45, "Charlie": 78, "David": 92, "Eve": 55}

# 13.1 Filter by value
passing = {k: v for k, v in scores.items() if v >= 60}
print(f"Passing scores: {passing}")

# 13.2 Filter by key
long_names = {k: v for k, v in scores.items() if len(k) > 3}
print(f"Long names: {long_names}")

# 13.3 Filter and transform
high_scores = {k: v*1.1 for k, v in scores.items() if v > 80}
print(f"High scores (boosted): {high_scores}")


print("\n" + "=" * 80)
print("PART 14: LAMBDA WITH DICTIONARIES")
print("=" * 80)

products = {"laptop": 1000, "phone": 500, "tablet": 300, "monitor": 400}

# 14.1 Sort by price (ascending)
by_price = sorted(products.items(), key=lambda x: x[1])
print("Products by price (ascending):")
for name, price in by_price:
    print(f"  {name}: ${price}")

# 14.2 Sort by name length
by_name_length = sorted(products.items(), key=lambda x: len(x[0]))
print("\nProducts by name length:")
for name, price in by_name_length:
    print(f"  {name} ({len(name)} chars): ${price}")

# 14.3 Filter with lambda
expensive = dict(filter(lambda x: x[1] > 400, products.items()))
print(f"\nExpensive items (>$400): {expensive}")


print("\n" + "=" * 80)
print("PART 15: PRACTICAL EXAMPLES")
print("=" * 80)

print("\n15.1 Example: Grade Management System")
print("-" * 80)

class GradeBook:
    def __init__(self):
        self.grades = {}
    
    def add_student(self, name, subject, grade):
        if name not in self.grades:
            self.grades[name] = {}
        self.grades[name][subject] = grade
    
    def get_average(self, name):
        if name in self.grades:
            grades = self.grades[name].values()
            return sum(grades) / len(grades) if grades else 0
        return 0
    
    def display_all(self):
        for name, subjects in self.grades.items():
            avg = self.get_average(name)
            print(f"  {name}: {subjects} (Avg: {avg:.2f})")

gb = GradeBook()
gb.add_student("Alice", "Math", 90)
gb.add_student("Alice", "Science", 85)
gb.add_student("Bob", "Math", 78)
gb.add_student("Bob", "Science", 82)

print("Grade Book:")
gb.display_all()


print("\n15.2 Example: Inventory System")
print("-" * 80)

inventory = {
    "apple": {"quantity": 50, "price": 0.5},
    "banana": {"quantity": 30, "price": 0.3},
    "orange": {"quantity": 20, "price": 0.6}
}

print("Inventory:")
total_value = 0
for item, details in inventory.items():
    value = details["quantity"] * details["price"]
    total_value += value
    print(f"  {item}: {details['quantity']} units @ ${details['price']} = ${value:.2f}")
print(f"Total inventory value: ${total_value:.2f}")


print("\n15.3 Example: Word Frequency Counter")
print("-" * 80)

text = "python programming is fun python is powerful python"
words = text.split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print(f"Text: {text}")
print("\nWord frequency:")
for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")


print("\n15.4 Example: Configuration Management")
print("-" * 80)

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin"
    },
    "api": {
        "host": "localhost",
        "port": 8000,
        "debug": True
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/app.log"
    }
}

def print_config(config, indent=0):
    for key, value in config.items():
        if isinstance(value, dict):
            print(" " * indent + f"{key}:")
            print_config(value, indent + 2)
        else:
            print(" " * indent + f"{key}: {value}")

print("Application Configuration:")
print_config(config)


print("\n15.5 Example: User Data Management")
print("-" * 80)

users = {
    "user1": {"name": "Alice", "email": "alice@example.com", "active": True},
    "user2": {"name": "Bob", "email": "bob@example.com", "active": False},
    "user3": {"name": "Charlie", "email": "charlie@example.com", "active": True}
}

# Find active users
active_users = {k: v for k, v in users.items() if v["active"]}
print(f"Active users: {list(active_users.keys())}")

# Get all emails
emails = [v["email"] for v in users.values()]
print(f"All emails: {emails}")

# Update all users
for user_id, user_data in users.items():
    user_data["updated"] = True

print(f"After update: {users['user1']}")


print("\n" + "=" * 80)
print("PART 16: COMMON DICTIONARY PATTERNS")
print("=" * 80)

print("""
Pattern 1: Grouping items by category
  students_by_year = {}
  for student in students:
      year = student['year']
      if year not in students_by_year:
          students_by_year[year] = []
      students_by_year[year].append(student)

Pattern 2: Building lookup tables
  user_ids = {user['email']: user['id'] for user in users}

Pattern 3: Counting occurrences
  from collections import Counter
  counts = Counter(items)

Pattern 4: Setting defaults
  config.setdefault('timeout', 30)
  config.setdefault('retries', 3)

Pattern 5: Merging configurations
  default_config = {'host': 'localhost', 'port': 8000}
  user_config = {'port': 9000}
  final_config = {**default_config, **user_config}

Pattern 6: Nested structure access
  try:
      value = data['user']['profile']['avatar']
  except KeyError:
      value = None

Pattern 7: Dictionary as cache
  cache = {}
  if key not in cache:
      cache[key] = expensive_operation(key)
  result = cache[key]
""")


print("\n" + "=" * 80)
print("PART 17: DICTIONARY SIZE AND MEMORY")
print("=" * 80)

import sys

empty = {}
small = {"a": 1, "b": 2}
medium = {f"key_{i}": i for i in range(100)}
large = {f"key_{i}": i for i in range(10000)}

print(f"Empty dict size: {sys.getsizeof(empty)} bytes")
print(f"Small dict (2 items): {sys.getsizeof(small)} bytes")
print(f"Medium dict (100 items): {sys.getsizeof(medium)} bytes")
print(f"Large dict (10000 items): {sys.getsizeof(large)} bytes")


print("\n" + "=" * 80)
print("PART 18: SUMMARY - QUICK REFERENCE")
print("=" * 80)

print("""
DICTIONARY OPERATIONS QUICK REFERENCE
=====================================

CREATION:
  d = {}                          # Empty dict
  d = {"key": "value"}            # With values
  d = dict()                      # Using constructor
  d = dict(a=1, b=2)              # Constructor with kwargs
  d = {x: x**2 for x in range(5)} # Comprehension

ACCESSING:
  value = d["key"]                # Direct access
  value = d.get("key")            # Safe access
  value = d.get("key", default)   # With default

MODIFICATION:
  d["key"] = value                # Set value
  d.update({"k": "v"})            # Update multiple
  d.setdefault("key", default)    # Set if not exists
  del d["key"]                    # Delete key
  d.pop("key")                    # Remove and return

ITERATION:
  for key in d:                   # Over keys
  for value in d.values():        # Over values
  for key, value in d.items():    # Over pairs

METHODS:
  d.keys()      - Get all keys
  d.values()    - Get all values
  d.items()     - Get key-value pairs
  d.get(k, v)   - Safe access with default
  d.pop(k)      - Remove key
  d.update(d2)  - Merge dicts
  d.clear()     - Remove all items
  d.copy()      - Shallow copy

COMMON PATTERNS:
  Grouping:     defaultdict(list)
  Counting:     Counter()
  Defaults:     setdefault()
  Filtering:    {k: v for k, v in d.items() if ...}
  Sorting:      sorted(d.items(), key=...)
  Merging:      {**d1, **d2}
""")

print("\n" + "=" * 80)
print("END OF COMPREHENSIVE DICTIONARY GUIDE")
print("=" * 80)
