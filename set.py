thisset = {"apple", "banana", "cherry"}
print(thisset)
#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#True and 1 is the same
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

normal_set = set(["a", "b","c"])
 
print("Normal Set")
print(normal_set)
 
# A frozen set
frozen_set = frozenset(["e", "f", "g"])
 
print("\nFrozen Set")
print(frozen_set)

# Creating a Set
people = {"Jay", "Idrish", "Archi"}
 
print("People:", end = " ")
print(people)
 
# This will add Daxit
# in the set
people.add("Daxit")
 
# Adding elements to the
# set using iterator
for i in range(1, 6):
    people.add(i)
 
print("\nSet after adding element:", end = " ")
print(people)

#here we learn these code in the class
print("start")
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
 
# Union using union()
# function
population = people.union(vampires)
 
print("Union using union() function")
print(population)