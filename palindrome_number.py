# Get a number from the user
n = int(input("Enter a number: "))

# Store the original number
original = n

# Initialize reverse
reverse = 0

# Reverse the number
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

# Check whether the number is palindrome
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
