# average of all element in array

def get_Avg(ar1):
    sum_total = sum(ar1)
    avg = sum_total / len(ar1)
    return avg

ar1 = [1, 2, 3, 4, 5]

avg1 = get_Avg(ar1)
print("The average of all element in array are", avg1)