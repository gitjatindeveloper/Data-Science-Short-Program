# removes duplicates from an array

def remove_duplicate(arr):
    return list(set(arr))

# Example usage
array = [11, 22, 33, 22, 44, 33, 44]
result = remove_duplicate(array)
print("Array", array,"after removing duplicates are", result)