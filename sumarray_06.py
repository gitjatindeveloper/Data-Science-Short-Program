# sum of all element in array

def get_Sum(ar1):
    sum = 0
    for num in ar1:
        sum += num
    return sum

ar1 = [1, 2, 3, 4, 5]

sum = get_Sum(ar1)
print("The sum of all element are", sum)