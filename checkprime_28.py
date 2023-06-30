# take a number as input and check whether it is prime or not

# function to check year is prime or not
def check_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Not Prime Number"
    return "Prime Number"

n = int(input("Enter a number: "))
check_num = check_prime(n)
print("The number", n, "is", check_num)