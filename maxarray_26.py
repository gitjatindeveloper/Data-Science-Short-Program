# find out maximum element in array

# function to find maximum element in array
def max_arr(n):
    max_n = n[0]
    for num in n:
        if num > max_n:
            max_n = num
    return max_n

n = [22, 45, 50, 10, 33]
max_n = max_arr(n)
print("The maximum element in", n,"is", max_n)