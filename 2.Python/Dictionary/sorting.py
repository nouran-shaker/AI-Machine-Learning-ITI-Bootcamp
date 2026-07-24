#Program to sort a dictionary by its values
my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

flipped_list = []
for key, value in my_dict.items():
    flipped_list.append([value, key])

flipped_list.sort()

ascending_dict = {}
for value, key in flipped_list:
    ascending_dict[key] = value

print("Sorted Dictionary:", ascending_dict)