# find second largest element in an array

def second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    
    largest = arr[0]
    second_largest = arr[0]
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == largest:
        return "No second-largest element found"
    
    return second_largest

array = [5, 8, 12, 4, 11]
result_secondlargest = second_largest(array)
print("The second largest element is", result_secondlargest)