# Program to check if a string is a palindrome
string = input("Enter a string: ")

cleaned_text = "".join(char for char in string if char.isalnum()).lower()

is_palindrome = cleaned_text == cleaned_text[::-1]

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")