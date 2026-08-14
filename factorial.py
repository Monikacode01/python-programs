# Factorial program in Python

# Get input from the user
num = int(input("Enter a number: "))

# Initialize factorial value
fact = 1

# Calculate factorial using a loop
for i in range(1, num + 1):
    fact = fact * i

# Display the result
print("Factorial of", num, "is", fact)
