"beau"
'beau'

name = "beauty"
phrase = "beauty is" + " a good girl"
phrase2 = name+" is a good"

name+=" is a good girl"

print(name)

aga = str(39)
print(aga) # this is a string


name = "beauty"

print(name[0]) # b
print(name[1]) # e
print(name[2]) # a
print(name[3]) # u
print(name[4]) # t
print(name[5]) # y

print(name[1:4]) # eau
print(name[:4]) # beau
print(name[2:5]) # aut








#  Python String Methods
# Here are the main string methods in Python, organized by category:
#  Case Conversion





"""
upper() - Convert to uppercase
•
lower() - Convert to lowercase
•
title() - Convert to title case
•
capitalize() - Capitalize first character
•
swapcase() - Swap case of all characters
 # Searching & Finding
•
find(sub) - Find index of substring (returns -1 if not found)
•
rfind(sub) - Find from the right
•
index(sub) - Like find, but raises ValueError if not found
•
count(sub) - Count occurrences of substring
•
startswith(prefix) - Check if starts with prefix
•
endswith(suffix) - Check if ends with suffix
 # Replacing
•
replace(old, new) - Replace all occurrences
•
translate() - Translate characters using a translation table
 # Splitting & Joining
•
split(sep) - Split by separator into list
•
rsplit(sep) - Split from the right
•
splitlines() - Split by line breaks
•
join(iterable) - Join iterable elements with string as separator
 # Trimming
•
strip() - Remove whitespace from both ends
•
lstrip() - Remove from left
•
rstrip() - Remove from right
 # Checking
•
isdigit() - Check if all characters are digits
•
isalpha() - Check if all characters are alphabetic
•
isalnum() - Check if all are alphanumeric
•
isspace() - Check if all are whitespace
•
isupper() / islower() - Check case
•
isidentifier() - Check if valid identifier
•
isdecimal() - Check if all are decimal
 # Formatting
•
format() - Format string with placeholders
•
format_map(dict) - Format using a dictionary
•
center(width) - Center string in field
•
ljust(width) - Left justify
•
rjust(width) - Right justify
•
zfill(width) - Pad with zeros
 # Other
•
encode() - Encode to bytes
•
expandtabs() - Expand tab characters
•
partition(sep) - Split into 3-tuple
•
rpartition(sep) - Partition from right
"""