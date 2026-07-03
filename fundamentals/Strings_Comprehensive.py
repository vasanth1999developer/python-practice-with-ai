"""
COMPREHENSIVE GUIDE TO PYTHON STRINGS AND ALL METHODS
======================================================
From Basic to Advanced with Examples for Every Method
"""

print("=" * 90)
print("PART 1: STRING BASICS")
print("=" * 90)

print("\n1.1 CREATING STRINGS")
print("-" * 90)

# Different ways to create strings
single_quote = 'hello'
double_quote = "hello"
triple_quote = """This is a
multi-line string"""

print(f"Single quotes: {single_quote}")
print(f"Double quotes: {double_quote}")
print(f"Triple quotes:\n{triple_quote}")

# String concatenation
name = "beauty"
phrase = "beauty is" + " a good girl"
phrase2 = name + " is a good"
phrase3 = name + " is a good girl"

print(f"\nConcatenation result: {phrase3}")

# Converting to string
age = 39
age_str = str(age)
print(f"Converted int to string: {age_str} (type: {type(age_str).__name__})")

print("\n1.2 INDEXING AND SLICING")
print("-" * 90)

name = "beauty"
print(f"String: {name}")
print(f"Index 0: {name[0]}")  # b
print(f"Index 1: {name[1]}")  # e
print(f"Index 2: {name[2]}")  # a
print(f"Index -1: {name[-1]}")  # y (last character)

print(f"\nSlice [1:4]: {name[1:4]}")  # eau
print(f"Slice [:4]: {name[:4]}")    # beau
print(f"Slice [2:5]: {name[2:5]}")  # aut
print(f"Slice [::2]: {name[::2]}")  # baty (every 2nd char)
print(f"Slice [::-1]: {name[::-1]}")  # ytuaeb (reversed)


print("\n" + "=" * 90)
print("PART 2: CASE CONVERSION METHODS")
print("=" * 90)

text = "Hello World"

print(f"Original: {text}")
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"title(): {text.title()}")
print(f"capitalize(): {text.capitalize()}")
print(f"swapcase(): {text.swapcase()}")

print("\n2.1 DETAILED CASE METHODS")
print("-" * 90)

# upper()
print("upper() - Convert all characters to uppercase")
text1 = "hello world"
print(f"  '{text1}'.upper() -> '{text1.upper()}'")

# lower()
print("\nlower() - Convert all characters to lowercase")
text2 = "HELLO WORLD"
print(f"  '{text2}'.lower() -> '{text2.lower()}'")

# title()
print("\ntitle() - Capitalize first letter of each word")
text3 = "hello world python"
print(f"  '{text3}'.title() -> '{text3.title()}'")

# capitalize()
print("\ncapitalize() - Capitalize first character only")
text4 = "hello world"
print(f"  '{text4}'.capitalize() -> '{text4.capitalize()}'")

# swapcase()
print("\nswapcase() - Swap case of all characters")
text5 = "Hello World"
print(f"  '{text5}'.swapcase() -> '{text5.swapcase()}'")


print("\n" + "=" * 90)
print("PART 3: SEARCHING AND FINDING METHODS")
print("=" * 90)

text = "The quick brown fox jumps over the lazy dog"

print(f"Text: {text}\n")

# find()
print("find() - Find first index of substring (returns -1 if not found)")
print(f"  find('quick'): {text.find('quick')}")
print(f"  find('dog'): {text.find('dog')}")
print(f"  find('cat'): {text.find('cat')}")

# rfind()
print("\nrfind() - Find last index of substring")
text_repeat = "the cat and the dog"
print(f"Text: {text_repeat}")
print(f"  rfind('the'): {text_repeat.rfind('the')}")
print(f"  find('the'): {text_repeat.find('the')}")

# index()
print("\nindex() - Like find(), but raises ValueError if not found")
print(f"  index('quick'): {text.index('quick')}")
try:
    text.index('cat')
except ValueError as e:
    print(f"  index('cat'): ValueError - {e}")

# count()
print("\ncount() - Count occurrences of substring")
text_count = "apple apple apple banana apple"
print(f"Text: {text_count}")
print(f"  count('apple'): {text_count.count('apple')}")
print(f"  count('an'): {text_count.count('an')}")

# startswith()
print("\nstartswith() - Check if string starts with prefix")
text_start = "Hello World"
print(f"Text: {text_start}")
print(f"  startswith('Hello'): {text_start.startswith('Hello')}")
print(f"  startswith('World'): {text_start.startswith('World')}")

# endswith()
print("\nendswith() - Check if string ends with suffix")
print(f"  endswith('World'): {text_start.endswith('World')}")
print(f"  endswith('Hello'): {text_start.endswith('Hello')}")


print("\n" + "=" * 90)
print("PART 4: REPLACING METHODS")
print("=" * 90)

# replace()
print("replace() - Replace occurrences of substring")
text = "cat and cat and dog"
print(f"Original: {text}")
print(f"replace('cat', 'dog'): {text.replace('cat', 'dog')}")
print(f"replace('cat', 'dog', 1): {text.replace('cat', 'dog', 1)}")  # Replace only first

# translate()
print("\ntranslate() - Translate characters using translation table")
original = "hello"
translation_table = str.maketrans("helo", "4310")
print(f"Original: {original}")
print(f"translate(table): {original.translate(translation_table)}")


print("\n" + "=" * 90)
print("PART 5: SPLITTING AND JOINING METHODS")
print("=" * 90)

# split()
print("split() - Split string into list by separator")
text = "apple,banana,orange,grape"
print(f"Text: {text}")
print(f"split(','): {text.split(',')}")

text2 = "hello   world   python"
print(f"\nText: '{text2}'")
print(f"split(): {text2.split()}")  # Default splits by whitespace

# rsplit()
print("\nrsplit() - Split from the right")
text3 = "a,b,c,d,e"
print(f"Text: {text3}")
print(f"split(',', 2): {text3.split(',', 2)}")
print(f"rsplit(',', 2): {text3.rsplit(',', 2)}")

# splitlines()
print("\nsplitlines() - Split by line breaks")
text_lines = "line1\nline2\nline3"
print(f"Text: {repr(text_lines)}")
print(f"splitlines(): {text_lines.splitlines()}")

# join()
print("\njoin() - Join list elements with string as separator")
words = ["apple", "banana", "orange"]
print(f"Words: {words}")
print(f"', '.join(words): {', '.join(words)}")
print(f"' - '.join(words): {' - '.join(words)}")


print("\n" + "=" * 90)
print("PART 6: TRIMMING METHODS")
print("=" * 90)

# strip()
print("strip() - Remove whitespace from both ends")
text = "  hello world  "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")
text2 = "***hello***"
print(f"\nOriginal: '{text2}'")
print(f"strip('*'): '{text2.strip('*')}'")

# lstrip()
print("\nlstrip() - Remove from left")
text3 = "  hello world  "
print(f"Original: '{text3}'")
print(f"lstrip(): '{text3.lstrip()}'")

# rstrip()
print("\nrstrip() - Remove from right")
text4 = "  hello world  "
print(f"Original: '{text4}'")
print(f"rstrip(): '{text4.rstrip()}'")


print("\n" + "=" * 90)
print("PART 7: CHECKING METHODS (is* methods)")
print("=" * 90)

# isdigit()
print("isdigit() - Check if all characters are digits")
print(f"  '12345'.isdigit(): {'12345'.isdigit()}")
print(f"  '123a5'.isdigit(): {'123a5'.isdigit()}")

# isalpha()
print("\nisalpha() - Check if all characters are alphabetic")
print(f"  'hello'.isalpha(): {'hello'.isalpha()}")
print(f"  'hello123'.isalpha(): {'hello123'.isalpha()}")

# isalnum()
print("\nisalnum() - Check if all are alphanumeric")
print(f"  'hello123'.isalnum(): {'hello123'.isalnum()}")
print(f"  'hello 123'.isalnum(): {'hello 123'.isalnum()}")

# isspace()
print("\nisspace() - Check if all are whitespace")
print(f"  '   '.isspace(): {'   '.isspace()}")
print(f"  'hello'.isspace(): {'hello'.isspace()}")

# isupper()
print("\nisupper() - Check if all cased characters are uppercase")
print(f"  'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"  'Hello'.isupper(): {'Hello'.isupper()}")

# islower()
print("\nislower() - Check if all cased characters are lowercase")
print(f"  'hello'.islower(): {'hello'.islower()}")
print(f"  'Hello'.islower(): {'Hello'.islower()}")

# isidentifier()
print("\nisidentifier() - Check if valid Python identifier")
print(f"  'variable_name'.isidentifier(): {'variable_name'.isidentifier()}")
print(f"  '123var'.isidentifier(): {'123var'.isidentifier()}")
print(f"  'var-name'.isidentifier(): {'var-name'.isidentifier()}")

# isdecimal()
print("\nisdecimal() - Check if all are decimal characters")
print(f"  '12345'.isdecimal(): {'12345'.isdecimal()}")
print(f"  '123.45'.isdecimal(): {'123.45'.isdecimal()}")

# isnumeric()
print("\nisnumeric() - Check if all are numeric characters")
print(f"  '12345'.isnumeric(): {'12345'.isnumeric()}")
print(f"  '½'.isnumeric(): {'½'.isnumeric()}")

# istitle()
print("\nistitle() - Check if string is titlecased")
print(f"  'Hello World'.istitle(): {'Hello World'.istitle()}")
print(f"  'hello world'.istitle(): {'hello world'.istitle()}")

# isprintable()
print("\nisprintable() - Check if all characters are printable")
print(f"  'hello'.isprintable(): {'hello'.isprintable()}")
print(f"  'hello\\n'.isprintable(): {repr('hello\n').isprintable()}")


print("\n" + "=" * 90)
print("PART 8: FORMATTING METHODS")
print("=" * 90)

# format()
print("format() - Format string with placeholders")
name = "Alice"
age = 25
result = "Name: {}, Age: {}".format(name, age)
print(f"  '{{}}, {{}}'.format('Alice', 25): {result}")

result2 = "Name: {0}, Age: {1}, Name again: {0}".format(name, age)
print(f"  With indices: {result2}")

result3 = "Name: {name}, Age: {age}".format(name="Bob", age=30)
print(f"  With keywords: {result3}")

# f-strings (modern approach)
print("\nf-strings (Python 3.6+)")
name = "Charlie"
age = 35
print(f"  f'Name: {name}, Age: {age}': Name: {name}, Age: {age}")

# center()
print("\ncenter() - Center string in field")
text = "hello"
print(f"  '{text}'.center(15): '{text.center(15)}'")
print(f"  '{text}'.center(15, '*'): '{text.center(15, '*')}'")

# ljust()
print("\nljust() - Left justify")
print(f"  '{text}'.ljust(15, '-'): '{text.ljust(15, '-')}'")

# rjust()
print("\nrjust() - Right justify")
print(f"  '{text}'.rjust(15, '-'): '{text.rjust(15, '-')}'")

# zfill()
print("\nzfill() - Pad with zeros")
number = "42"
print(f"  '{number}'.zfill(5): '{number.zfill(5)}'")
print(f"  '{'-42'}'.zfill(5): '{'-42'.zfill(5)}'")


print("\n" + "=" * 90)
print("PART 9: PARTITION METHODS")
print("=" * 90)

# partition()
print("partition() - Split into 3-tuple (before, sep, after)")
text = "hello-world-python"
print(f"Text: {text}")
print(f"  partition('-'): {text.partition('-')}")

# rpartition()
print("\nrpartition() - Partition from right")
print(f"  rpartition('-'): {text.rpartition('-')}")


print("\n" + "=" * 90)
print("PART 10: ENCODING AND OTHER METHODS")
print("=" * 90)

# encode()
print("encode() - Encode string to bytes")
text = "hello"
encoded = text.encode()
print(f"  'hello'.encode(): {encoded}")
print(f"  Type: {type(encoded).__name__}")

encoded_utf8 = text.encode('utf-8')
print(f"  'hello'.encode('utf-8'): {encoded_utf8}")

# expandtabs()
print("\nexpandtabs() - Expand tab characters")
text_tab = "hello\tworld\tpython"
print(f"Original: {repr(text_tab)}")
print(f"expandtabs(): {repr(text_tab.expandtabs())}")
print(f"expandtabs(4): {repr(text_tab.expandtabs(4))}")

# swapcase()
print("\nswapcase() - Swap case")
text_case = "HeLLo WoRLd"
print(f"  '{text_case}'.swapcase(): '{text_case.swapcase()}'")


print("\n" + "=" * 90)
print("PART 11: ADVANCED EXAMPLES - PRACTICAL USAGE")
print("=" * 90)

print("\n11.1 EXAMPLE: Validate Email")
print("-" * 90)

def is_valid_email(email):
    """Check if email is valid format"""
    return "@" in email and "." in email and email.count("@") == 1

emails = ["user@example.com", "invalid.email", "test@domain", "user@@example.com"]
for email in emails:
    print(f"  {email}: {is_valid_email(email)}")

print("\n11.2 EXAMPLE: Parse CSV Data")
print("-" * 90)

csv_line = "Alice,25,Engineer,New York"
fields = csv_line.split(",")
print(f"CSV: {csv_line}")
print(f"Parsed fields: {fields}")
print(f"  Name: {fields[0]}, Age: {fields[1]}, Job: {fields[2]}")

print("\n11.3 EXAMPLE: Clean and Normalize Text")
print("-" * 90)

def clean_text(text):
    """Clean and normalize text"""
    return text.strip().lower().replace("  ", " ")

messy_texts = ["  Hello   World  ", "  PYTHON   PROGRAMMING  "]
for text in messy_texts:
    print(f"  '{text}' -> '{clean_text(text)}'")

print("\n11.4 EXAMPLE: Extract File Extension")
print("-" * 90)

files = ["document.pdf", "image.jpg", "script.py", "archive.tar.gz"]
for filename in files:
    if "." in filename:
        name, ext = filename.rsplit(".", 1)
        print(f"  {filename} -> Name: {name}, Extension: {ext}")

print("\n11.5 EXAMPLE: Format Output Table")
print("-" * 90)

students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
print("Student Grades:")
print("-" * 30)

for name, grade in students:
    padded_name = name.ljust(15)
    padded_grade = str(grade).rjust(5)
    print(f"  {padded_name} {padded_grade}")

print("\n11.6 EXAMPLE: Password Validation")
print("-" * 90)

def validate_password(pwd):
    """Check password strength"""
    checks = {
        "Length >= 8": len(pwd) >= 8,
        "Has uppercase": any(c.isupper() for c in pwd),
        "Has lowercase": any(c.islower() for c in pwd),
        "Has digit": any(c.isdigit() for c in pwd),
    }
    return checks

passwords = ["weak", "Medium123", "Strong@Pass123"]
for pwd in passwords:
    print(f"\nPassword: {pwd}")
    checks = validate_password(pwd)
    for check, result in checks.items():
        status = "[OK]" if result else "[FAIL]"
        print(f"  {status} {check}")


print("\n" + "=" * 90)
print("PART 12: STRING METHODS QUICK REFERENCE")
print("=" * 90)

print("""
CASE METHODS
============
upper()         -> Convert to uppercase
lower()         -> Convert to lowercase  
title()         -> Capitalize first letter of each word
capitalize()    -> Capitalize first character
swapcase()      -> Swap case of all characters

SEARCHING METHODS
=================
find(sub)       -> Find first index (returns -1)
rfind(sub)      -> Find last index
index(sub)      -> Find index (raises ValueError)
count(sub)      -> Count occurrences
startswith(pre) -> Check if starts with prefix
endswith(suf)   -> Check if ends with suffix

REPLACING METHODS
=================
replace(old, new) -> Replace all occurrences
translate(table)  -> Translate characters

SPLITTING/JOINING METHODS
==========================
split(sep)      -> Split by separator
rsplit(sep)     -> Split from right
splitlines()    -> Split by line breaks
join(iterable)  -> Join elements with string as separator

TRIMMING METHODS
================
strip()         -> Remove whitespace both ends
lstrip()        -> Remove from left
rstrip()        -> Remove from right

CHECKING METHODS (is* methods)
==============================
isdigit()       -> All characters are digits
isalpha()       -> All characters are alphabetic
isalnum()       -> All are alphanumeric
isspace()       -> All are whitespace
isupper()       -> All cased chars are uppercase
islower()       -> All cased chars are lowercase
isidentifier()  -> Valid Python identifier
isdecimal()     -> All are decimal
isnumeric()     -> All are numeric
istitle()       -> String is titlecased
isprintable()   -> All characters are printable

FORMATTING METHODS
==================
format()        -> Format with placeholders
center(w)       -> Center in field
ljust(w)        -> Left justify
rjust(w)        -> Right justify
zfill(w)        -> Pad with zeros

OTHER METHODS
=============
encode()        -> Encode to bytes
expandtabs()    -> Expand tabs
partition(sep)  -> Split into 3-tuple
rpartition(sep) -> Partition from right
""")


print("\n" + "=" * 90)
print("PART 13: SUMMARY TABLE OF ALL STRING METHODS")
print("=" * 90)

print("""
METHOD          RETURNS     MODIFIES    EXAMPLE
------          -------     --------    -------
upper()         str         No          'hello'.upper() -> 'HELLO'
lower()         str         No          'HELLO'.lower() -> 'hello'
title()         str         No          'hello world'.title() -> 'Hello World'
capitalize()    str         No          'hello'.capitalize() -> 'Hello'
swapcase()      str         No          'HeLLo'.swapcase() -> 'hEllO'
find()          int         No          'hello'.find('l') -> 2
rfind()         int         No          'hello'.rfind('l') -> 3
index()         int         No          'hello'.index('l') -> 2
count()         int         No          'hello'.count('l') -> 2
startswith()    bool        No          'hello'.startswith('h') -> True
endswith()      bool        No          'hello'.endswith('o') -> True
replace()       str         No          'hello'.replace('l', 'L') -> 'heLLo'
split()         list        No          'a b c'.split() -> ['a', 'b', 'c']
join()          str         No          ', '.join(['a', 'b']) -> 'a, b'
strip()         str         No          ' hello '.strip() -> 'hello'
lstrip()        str         No          ' hello'.lstrip() -> 'hello'
rstrip()        str         No          'hello '.rstrip() -> 'hello'
isdigit()       bool        No          '123'.isdigit() -> True
isalpha()       bool        No          'abc'.isalpha() -> True
isalnum()       bool        No          'abc123'.isalnum() -> True
isspace()       bool        No          '   '.isspace() -> True
isupper()       bool        No          'HELLO'.isupper() -> True
islower()       bool        No          'hello'.islower() -> True
format()        str         No          '{}'.format('hi') -> 'hi'
encode()        bytes       No          'hello'.encode() -> b'hello'
partition()     tuple       No          'a-b'.partition('-') -> ('a', '-', 'b')
""")

print("\n" + "=" * 90)
print("END OF COMPREHENSIVE STRING GUIDE")
print("=" * 90)
