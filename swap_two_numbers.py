# Swap Two Numbers

# Get two numbers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Display numbers before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the values
a, b = b, a

# Display numbers after swapping
print("After swapping:")
print("a =", a)
print("b =", b)
