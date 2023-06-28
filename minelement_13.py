def get_min(ar1):
    getmin = ar1[0]
    for num in ar1:
        if num < getmin:
         getmin = num
    return getmin

ar1 = [77, 66, 22, 88, 11]

min1 = get_min(ar1)
print("The smallest element in array are", min1)