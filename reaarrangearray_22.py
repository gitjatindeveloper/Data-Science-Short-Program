# rearrange array where left means negative values to positive values

def rearrange_array(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    return arr

array = [5, -5, 1, -4, -7, 8, -2]
rearranged_array = rearrange_array(array)
print("The array", array," into Rearranged array:", rearranged_array)