# Sum of First N Natural Numbers

# Get a number from the user
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Calculate the sum
for i in range(1, n + 1):
    total = total + i

# Display the result
print("Sum:", total)
