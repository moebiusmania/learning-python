# basics.py
# Basic data types and variables
name = "John"
age = 25
height = 1.75
is_student = True

# Print different types
print("String:", name)
print("Integer:", age)
print("Float:", height)
print("Boolean:", is_student)

# Basic arithmetic
x = 10
y = 3
print("\nArithmetic Operations:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Integer Division:", x // y)
print("Modulus:", x % y)
print("Power:", x ** y)

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("\nString Operations:")
print("Full name:", full_name)
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Name length:", len(full_name))

# Lists
fruits = ["apple", "banana", "orange"]
print("\nList Operations:")
print("Original list:", fruits)
fruits.append("grape")
print("After append:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("List length:", len(fruits))

# Conditional statements
age = 18
print("\nConditional Example:")
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Simple function
def greet(name):
    return f"Hello, {name}!"

print("\nFunction Example:")
print(greet("Alice"))

# Loop examples
print("\nLoop Examples:")
for fruit in fruits:
    print(f"I like {fruit}")

for i in range(3):
    print(f"Count: {i}")