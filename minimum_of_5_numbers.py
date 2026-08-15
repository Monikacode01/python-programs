# Find Minimum Among 5 Numbers

# Get five numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

# Assume the first number is the minimum
minimum = num1

# Compare the second number
if num2 < minimum:
    minimum = num2

# Compare the third number
if num3 < minimum:
    minimum = num3

# Compare the fourth number
if num4 < minimum:
    minimum = num4

# Compare the fifth number
if num5 < minimum:
    minimum = num5

# Display the minimum number
print("Minimum number:", minimum)
