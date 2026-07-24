#Program to take a list and print a new one with the even numbers only
Sample_List=[1,2,3,4,5,6,7,8,9]
Even_Numbers=[]
for i in range (0,9):
    if Sample_List[i]%2==0:
        Even_Numbers.append(Sample_List[i])
print(Even_Numbers)
