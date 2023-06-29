# find the majority element in array of interger

def majority_element(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    # Verify if the candidate is the majority element
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > len(arr) // 2:
        return candidate
    else:
        return "No majority element found"

# Example usage
array = [3, 8, 3, 3, 6, 3, 1]
majority_elements = majority_element(array)
print(" The majority element in", array,"is", majority_elements)