# find maximum element in array

def get_Max(ar1):
    max_num = ar1[0]
    for num in ar1:
        if num > max_num:
         max_num = num
    return max_num

ar1 = [1, 2, 3, 4, 5]

max1 = get_Max(ar1)
print("The largest element in array are", max1)