# Fibonacci series program in Python

# Get input from the user
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a = 0
b = 1

# Display Fibonacci series
print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
