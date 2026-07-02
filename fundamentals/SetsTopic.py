#sets

my_set = {1, 2, 3, 4, 5}

print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set1 = {"apple", "banana", "cherry"}
my_set2 = {"banana", "cherry", "date", "elderberry"}

interset = my_set2 & my_set1
print(interset)  # Output: {'banana', 'cherry'}

mod = my_set2 - my_set1
print(mod)  # Output: {'date', 'elderberry'}

mod2 = my_set1 | my_set2
print(mod2)  # Output: {'apple', 'banana', 'cherry', 'date', 'elderberry'}

mod3 = my_set1 ^ my_set2
print(mod3)  # Output: {'apple', 'date', 'elderberry'}

mod4 = my_set1.union(my_set2)
print(mod4)  # Output: {'apple', 'banana', 'cherry', 'date', 'elderberry'}

my_set3 ={"apple", "banana", "cherry", "date", "elderberry","apple"}
print(my_set3)  # Output: {'apple', 'banana', 'cherry', 'date', 'elderberry'} (duplicates are removed)



