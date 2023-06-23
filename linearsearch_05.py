# linear search for target element

def linear_search(ar_1, target_1):
    for i in range(len(ar_1)):
        if ar_1[i] == target_1:
            return i
    return -1

ar_1 = [3, 5, 8, 6, 2]
target_1 = 2

task_1 = linear_search(ar_1, target_1)

if task_1 != -1:
    print("Target element", target_1,"found at index", task_1)
else:
    print("Target element", target_1,"not found in the array")