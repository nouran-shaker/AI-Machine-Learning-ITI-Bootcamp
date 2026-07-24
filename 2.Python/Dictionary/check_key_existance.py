#program to check if a key exists in a dictionary
my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}
key_to_check = 'banana'

if key_to_check in my_dict:
    print("The key", key_to_check, "exists in the dictionary.")
else:
    print("The key", key_to_check, "does not exist in the dictionary.")