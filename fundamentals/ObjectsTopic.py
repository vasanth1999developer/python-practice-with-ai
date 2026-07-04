age = 8

print(age.real)
print(age.imag)
print(age.bit_length())


items = [1, 2, 3, 4, 5]

items.append(6)
print(items)  # Output: [1, 2, 3, 4, 5, 6]
items.pop() # Output: 6
print(items)  # Output: [1, 2, 3, 4, 5]
items.remove(3)
print(items)  # Output: [1, 2, 4, 5]

print (id(items))  # Output: 140234567890

items = [7, 8, 9]
print (id(items))  # Output: 140234567891 (different from the previous