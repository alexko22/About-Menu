# Task 1: Menu of Recursive Functions
print("Welcome to the Number Program! Please select an option.")
val = int(input("1. Calculate Factorial, 2. Find the nth Fibonacci Number, 3. Exit. Pick an option: "))

# Task 2 / 3: Fibonacci and Factorial
# Same functions as previous assignment
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
# Same functions as previous assignment
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-2) + fibonacci(x-1)

# Handling what to do
if (val == 1 or val == 2):
    val2 = int(input("Enter a number for this operation: "))
if (val == 3):
    print("Exiting the Program. Thank you!")

if (val == 1):
    print("The factorial value is", factorial(val2))
elif (val == 2):
    print("The fibonacci value is", fibonacci(val2))