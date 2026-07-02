name = ["Alice", "Bob", "Charlie",True,1,2,3,4,5]

name[2]="David"  # Changing the third element from "Charlie" to "David"

name.append("Eve")  # Adding a new element "Eve" to the end of the list

name.extend(["Frank", "Grace"])  # Adding multiple elements to the end of the list

name.extend(["vasu", 4]) # Adding multiple elements to the end of the list
print(name[0])  # Output: Alice
print(name[1])  # Output: Bob
print(name[2])  # Output: David

name += ["vasu"]  # Adding a string to the list (will be treated as individual characters)

print(name[-1])  # Output: 5
print(name[-2])  # Output: 4

print("Length of the list:", len(name))  # Output: Length of the list: 9

print("Alice" in name)  # Output: True

name.remove("Bob")  # Removing "Bob" from the list

print(name.pop())

print(name)  # Output: ['Alice', 'David', 'Eve', 'Frank', 'Grace', 'vasu', 4, 5]


items = ["apple", "banana", "cherry", "date", "elderberry"]
# Accessing elements using positive indexing
print(items[0])  # Output: apple
print(items[1])  # Output: banana
print(items[2])  # Output: cherry

items.index("banana")  # Output: 1 (index of "banana")
items.insert(2, "blueberry")  # Inserts "blueberry" at index 2
items.sort()  # Sorts the list in ascending order
items.sort(key=str.lower)  # Sorts the list in ascending order (case-insensitive)

itemscopy = items.copy()  # Creates a shallow copy of the list
itemscopy2 = items[:]  # Creates a shallow copy of the list using slicing
print(items)
