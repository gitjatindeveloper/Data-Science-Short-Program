# factorial of a number

n = 10

if n < 0:
    print("The factorial of", n, "is not defined for negative numbers")
elif n == 0 or n == 1:
    print("The factorial of", n, "is 1")
else:
    result = 1
    for i in range(2, n + 1):
        result *= i
    print("The factorial of", n, "is", result)