# factorial of number

number_01 = int(input("Enter number: "))
factorial = 1

if number_01 < 0:
    print("Factorial of", number_01,"doesn't exist for negative values")
elif number_01 == 0:
    print("Factorial of", number_01,"is 1")
else:
    for i in range(1, number_01 + 1):
        factorial *= i
    print("Factorial of", number_01,"is", factorial)