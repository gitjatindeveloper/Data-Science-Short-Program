# find minimum element in array

def get_Min(ar1):
    min_num = ar1[0]
    for num in ar1:
        if num < min_num:
         min_num = num
    return min_num

ar1 = [1, 2, 3, 4, 5]

min1 = get_Min(ar1)
print("The largest element in array are", min1)