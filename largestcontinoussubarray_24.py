# find the largest continous subarray with non negative sum

def find_subarray(arr):
    max_sum = 0
    current_sum = 0

    for num in arr:
        current_sum += num

        if current_sum < 0:
            current_sum = 0

        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
array = [1, -5, 3, -2, 8, -9, 7, 6]
largest_sum = find_subarray(array)
print("Largest non-negative subarray sum:", largest_sum)