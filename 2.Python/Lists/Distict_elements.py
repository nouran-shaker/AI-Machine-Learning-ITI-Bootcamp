# Program to print distinct elements from a list
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
distinct_list = []

for x in sample_list:
    if x not in distinct_list:
        distinct_list.append(x)

print(distinct_list)