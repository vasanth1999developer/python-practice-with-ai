#Dictionaries
from fundamentals.TuplesTopic_Comprehensive import student

dog ={"name": "Buddy", "age": 3, "breed": "Golden Retriever"}
print(dog["name"])  # Output: Buddy
print(dog["age"])   # Output: 3
print(dog["breed"]) # Output: Golden Retriever

student = {"name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "courses": ["Data Structures", "Algorithms", "Databases"],
    "is_graduated": False}
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 20
print(student["major"]) # Output: Computer Science
print(student["courses"]) # Output: ['Data Structures', 'Algorithms', 'Databases']
print(student["is_graduated"]) # Output: False

print(list(student.keys()))  # Output: ['name', 'age', 'major', 'courses', 'is_graduated']
print(list(student.values()))  # Output: ['Alice', 20, 'Computer Science', ['Data Structures', 'Algorithms', 'Databases'], False]
print(list(student.items()))  # Output: [('name', 'Alice'), ('age', 20), ('major', 'Computer Science'), ('courses', ['Data Structures', 'Algorithms', 'Databases']), ('is_graduated', False)]

student["age"] = 21  # Updating the age
student["is_graduated"] = True  # Updating the graduation status
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'courses': ['Data Structures', 'Algorithms', 'Databases'], 'is_graduated': True}
student["GPA"] = 3.8  # Adding a new key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'courses': ['Data Structures', 'Algorithms', 'Databases'], 'is_graduated': True, 'GPA': 3.8}
del student["major"]  # Deleting the major key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 21, 'courses': ['Data Structures', 'Algorithms', 'Databases'], 'is_graduated': True, 'GPA': 3.8}