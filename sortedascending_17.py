# check whether array is sorted in ascending order

def array_sorted(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [5, 3, 2, 1, 4]

result1 = array_sorted(array1)
print("Array1 is sorted:-", result1)

result2 = array_sorted(array2)
print("Array2 is sorted:-", result2)