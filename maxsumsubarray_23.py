# find subarray with the maximum sum

def maximum_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


array = [-1, 2, -6, 5, -2, 5, 3, -9, 8]
maximum_subarray_sum = maximum_subarray(array)
print("Maximum subarray sum:", maximum_subarray_sum)