# average of all element in array

def total_Avg(arr1):
    sum_total = sum(arr1)
    avg = sum_total / len(arr1)
    return avg

arr1 = [1, 2, 3, 4, 10]

avg1 = total_Avg(arr1)
print("The average of all element in array are", avg1)