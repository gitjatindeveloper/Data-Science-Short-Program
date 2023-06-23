# fibonacci series for given number of terms

number = int(input("Enter the number of terms: "))

first_terms = 0
second_terms = 1

print("fibonacci series for", number, "of terms")

for i in range(number):
    print(first_terms)
    next_terms = first_terms + second_terms
    first_terms = second_terms
    second_terms = next_terms
