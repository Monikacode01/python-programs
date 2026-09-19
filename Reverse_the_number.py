# Get a number from the user
n = int(input("Enter a number: "))

# Initialize reverse
reverse = 0

# Reverse the number
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

# Display the result
print("Reverse:", reverse)
