from fundamentals.ControlStatements import condition

condition = True


# while condition:
#     print("This is a while loop.")
#     user_input = input("Do you want to continue? (yes/no): ")
#     if user_input.lower() != "yes":
#         condition = False

count = 0
while count <=    5:
    print(f"Count is: {count}")
    count += 1


items = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

for item in items:
    print(item)

for index ,items in enumerate(items):
    print(f"Index: {index}, Item: {items}")


for i  in range(5):
    print(f"Iteration {i}")

