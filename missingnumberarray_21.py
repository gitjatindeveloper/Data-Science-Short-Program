# find missing number in an array in consercutive integers

def missing_number(arr):
    n = len(arr) + 1
    expect_n = n * (n + 1) // 2
    actual_n = sum(arr)
    missing_n = expect_n - actual_n
    return missing_n

arr_1 = [1, 2, 4, 5, 6]
missing_result = missing_number(arr_1)
print("The missing number", arr_1, "is", missing_result)