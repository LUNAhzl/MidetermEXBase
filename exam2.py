#Create a function that takes one argument which is a list and returns a list
#removed of all the odd numbers and the number 10s.

def remove_odd_and_tens(lst):
    return [num for num in lst if num % 2 == 0 and num != 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = remove_odd_and_tens(numbers)
print(result)
