# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]
 
# Display list
print(Lst[-7::1])

print(Lst[5::6])


# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# Show original list
print("Original List:\n", List)
 
print("\nSliced Lists: ")
 
# Creating new List
newList = List[:3]+List[7:]
 
# Display sliced list
print(newList)
 
# Changing existing List
List = List[::2]+List[1::2]
 
# Display sliced list
print(List)


