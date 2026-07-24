#Program to find the kth largest element in a list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

n = len(sample_list)

for i in range(n):
    for j in range(0, n - i - 1):
        
        if sample_list[j] < sample_list[j+1]:
            sample_list[j], sample_list[j+1] = sample_list[j+1], sample_list[j]

print("The " ,k ,"th largest element is:" , sample_list[k-1])