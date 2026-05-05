#TODO:Used to store a collection of data and Once a set is created, you cannot change its items, but you can remove items and add new items.

# mySet = {
#     "Ankit","Abijit","Sweety","Ankit"  # dublicates not allowed!
# }
# print(mySet)
# print(len(mySet))


# set can be created using set keyword

name = "Ankit","Abhijit","Sweety"
# print(type(name))
# names = set(name)
# print(names)
# print(type(names))

# accessing set items : no index so use loops

# mySet = {
#     "Ankit","Abijit","Sweety","Ankit"  # dublicates not allowed!
# }
# for x in mySet:
#     print(x)

# print("Ankit" in mySet)    

# # adding items:


# mySet.add("Anammika")
# print(mySet)

# list1 = [1,2,3]
# mySet.update(list1)
# print(mySet)


# joining two sets: 

# set1 = {1,2,3}
# set2={4,5,6}

# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)


# frozen set

# x = frozenset({1,2})
# print(x)

# Inside the editor, complete the following steps:
# Create a set called colors with the values "red", "green", "blue"
# Print the set
# Add "yellow" to the set using add()
# Remove "green" from the set using discard()
# Print the number of items using len()

colors = {"red", "green","blue"}
print(colors)
colors.add("yellow")
print(colors)
colors.discard("green")
print(colors)
print(len(colors))