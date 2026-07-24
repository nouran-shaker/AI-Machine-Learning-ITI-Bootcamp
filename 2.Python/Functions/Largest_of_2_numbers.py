#function to return the largest of 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def largest_of_2_numbers(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print("The largest number is:", largest_of_2_numbers(num1, num2))
