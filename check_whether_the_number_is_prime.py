# Get a number from the user
n = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True

# Check for factors
if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")
