#Create a function that takes 2D lists(lists within lists).
#If the first element of the list is an even number,
#add all elements to the variable named total. Return the value of the total.

def calculate_total(lst):
    total = 0
    for sublist in lst:
        if sublist[0] % 2 == 0:
            total += sum(sublist)
    return total

list1 = [[2, 4, 6], [1, 3, 5], [8, 10, 12]]
result1 = calculate_total(list1)
print(result1)
