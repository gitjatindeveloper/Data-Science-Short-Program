# count the number of occurance of specfic element in an array

def count_specific(ar1, target):
    count_target = 0
    for num in ar1:
        if num == target:
            count_target += 1
    return count_target 

ar1 = [1, 2, 3, 1, 5]
target = 1

count_target = count_specific(ar1, target)
print("The number of occurance of", target,"in array are", count_target)