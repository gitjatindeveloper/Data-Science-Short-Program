# count the number of occurance of specfic element in an array

def find_element(array1, target):
    find_target = 0
    for num in array1:
        if num == target:
            find_target += 1
    return find_target 

array1 = [22, 11, 44, 33, 44]
target = 44

count_target = find_element(array1, target)
print("The number of occurance of", target,"in array are", count_target)