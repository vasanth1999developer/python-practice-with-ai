# ============================================
# STRING TYPE CHECKING
# ============================================
name = "string"
print(isinstance(name, str))

# ============================================
# INTEGER TYPE CHECKING
# ============================================
age = 25
print(isinstance(age, int))

# ============================================
# FLOAT TYPE CHECKING
# ============================================
height = 5.9
print(isinstance(height, float))

# ============================================
# TYPE CONVERSION: int to float
# ============================================
age = float(25)
print(isinstance(age, float))

# ============================================
# TYPE CONVERSION: string to int (valid)
# ============================================
num = "20"
age = int(num)
print(isinstance(num, int))

# ============================================
# TYPE CONVERSION: string to int (invalid)
# ============================================
# ValueError: invalid literal for int() with base 10: 'two'
# num = "two"
# age = int(num)

# ============================================
# OTHER DATA TYPES (Not yet covered)
# ============================================
# complex - Complex numbers
# bool - Booleans
# list - Lists
# tuple - Tuples
# range - Ranges
# dict - Dictionaries
# set - Sets