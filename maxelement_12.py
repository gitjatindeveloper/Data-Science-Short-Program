def get_Max(ar1):
    getmax = ar1[0]
    for num in ar1:
        if num > getmax:
         getmax = num
    return getmax

ar1 = [22, 33, 11, 55, 44]

getmax = get_Max(ar1)
print("The largest element in array are", getmax)