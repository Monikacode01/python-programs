# Get a number from the user
n = int(input("Enter a number: "))

# Store the original number
original = n

# Count the number of digits
digits = len(str(n))

# Initialize sum
total = 0

# Calculate Armstrong sum
while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

# Check whether the number is Armstrong
if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
