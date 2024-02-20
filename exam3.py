#Create a program wherein the user will input a String that represents
#multiplication of two numbers then print out the result.


input_string = input("Input: ")
num1, num2 = input_string.split("*")

num1 = int(num1)
num2 = int(num2)

result = num1 * num2

print("Result:", result)
