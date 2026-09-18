# Sum of Odd Numbers

# Get the limit from the user
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Add odd numbers
for i in range(1, n + 1, 2):
    total = total + i

# Display the result
print("Sum of odd numbers:", total)
