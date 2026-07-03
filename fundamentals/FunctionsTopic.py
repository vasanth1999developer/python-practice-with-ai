#Function

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


def hello_world():
    print("Hello, World!")

hello_world()
hello_world()
hello_world()

def student_info(name, age, major):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Major: {major}")

student_info("Alice", 20, "Computer Science")

def car(tuplevalues):
    make, model, year = tuplevalues
    print(f"Car Make: {make}")
    print(f"Car Model: {model}")
    print(f"Car Year: {year}")

car(("Toyota", "Camry", 2020))



def add_numbers(a, b):
    return a + b

add_numbers(5, 10)  # Output: 15
# add_numbers() ## Output: TypeError: add_numbers() missing 2 required positional arguments: 'a' and 'b'


def change_name(name):
    name = "Bob"
    print(f"Inside function: {name}")

name = "Alice"
change_name(
name
)
print(f"Outside function: {name}")  # Output: Outside function: Alice