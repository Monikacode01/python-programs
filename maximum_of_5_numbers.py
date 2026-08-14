# Find Maximum Number Among 5 Numbers

# Get 5 numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))

# Assume the first number is the maximum
maximum = a

# Compare with the remaining numbers
if b > maximum:
    maximum = b

if c > maximum:
    maximum = c

if d > maximum:
    maximum = d

if e > maximum:
    maximum = e

# Display the maximum number
print("Maximum number is:", maximum)
