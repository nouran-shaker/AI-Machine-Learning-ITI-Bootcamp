#Program to take list of 10 items and store them in a list
Shopping_List=[]
for i in range (0,10):
    item=input("Enter the item:")
    Shopping_List.append(item)
print("The shopping list is:", Shopping_List)
print("The second item in the list is:", Shopping_List[1])
print("The eighth item in the list is:", Shopping_List[7])
new_item=input("Enter the new item to be added:")
Shopping_List.append(new_item)
print("The updated shopping list is:", Shopping_List)