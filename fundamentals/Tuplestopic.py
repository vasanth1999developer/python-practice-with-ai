#Tuples

name = ("Alice", "Bob", "Charlie", True, 1, 2, 3, 4, 5,"Bob")

print(name[0])

name.index("Bob")  # Output: 1 (index of "Bob")

name.index("Charlie")  # Output: 2 (index of "Charlie")

name.count("Bob")  # Output: 2 (count of "Bob" in the tuple)

print("Length of the tuple:", len(name))  # Output: Length of the tuple: 10

print("bob" in name)  # Output: True

newname = name + ("David",)  # Adding a new element "David" to the tuple




