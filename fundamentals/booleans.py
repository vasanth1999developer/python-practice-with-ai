
Done = True

print(type(Done)==bool)

if Done:
    print("Done")
else:
    print("Not Done")


# Boolean conversion
print(bool(1))           # True
print(bool(0))           # False
print(bool("hello"))     # True
print(bool(""))          # False

# Logical operations
print(True and False)    # False
print(True or False)     # True
print(not True)          # False

# all() and any()
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(any([False, False, True]))  # True

# isinstance()
print(isinstance(5, int))         # True
print(isinstance("hello", str))   # True

# Comparison
print(5 > 3)             # True
print(10 == "10")        # False


