# fruits = ("Apple", "Banana", "Apple","Mango", "Strawberry", "Grapes", "Watermelon", "Pineapple","Banana", "Peach", "Cherry", "Blueberry")

# print(fruits[2:5])  #! 5th index is expelled: watermelon is not printed!

# # * inserting items inside a tuple:

# temp = list(fruits)
# temp.append("Cranberry")
# fruits = tuple(temp)
# print(fruits)

# #* unpacking the tuple:

# # (one,two,three) = fruits
# # print(one)


# # looping inside a tuple:

# # for x in fruits:
# #     print(x)


# # for x in range(len(fruits)):
# #     print(x)

 #! joining the tuples:

# # tuple1 = ("Ankit","unsaa","chotu")
# # tuple2 = ("Sushma", " grace")
# # tuple3 = tuple1+tuple2
# # print(tuple3)

# print(fruits.count("Apple"))
# print(fruits.index("Banana"))



fruits = ("Apple", "Banana", "Mango", "Strawberry")
(x,*y) = fruits
print(y)
fruits = fruits**2
print(fruits)