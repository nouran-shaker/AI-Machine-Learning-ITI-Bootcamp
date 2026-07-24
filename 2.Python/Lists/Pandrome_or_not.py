#Program to take list and check whether it is palindrome or not
sample_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]
reversed_list = sample_list[::-1]

if sample_list == reversed_list:
    print("True")
else:
    print("False")