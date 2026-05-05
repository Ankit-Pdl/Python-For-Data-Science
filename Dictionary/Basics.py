# # key value pair vako data store garnako lagi dictionary use hunchha

# myDisctionary = {
#     "Name":"Ankit",
#     "Age":12,
#     "Address": "Sanothimi",
#     "Semester:": "Fourth"
# }

# print(myDisctionary)

 #! Dictionary items are ordered, changeable, and do not allow duplicates.

# print(myDisctionary["Name"])


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# myTuple = (1,2,3,4,3)
# print(myTuple)


# #! accessing data in dictionary

# employees = {
#     "Name": "Abhishek",
#     "Age": 19,
#     "Profession": "Software Engineer"

# }

# print(employees.get("Name"))
# print(employees["Age"])
# print(employees.keys())

# # adding new Items to the dictionary

# employees["Address"] = "Bhaktapur"
# print(employees)

# #! changing dictionary values
# employees = {
#      "Name": "Abhishek",
#      "Age": 19,
#      "Profession": "Software Engineer"

#  }

# employees["Name"] = "Ankit"
# print(employees)

# employees.update({"Name":"Anamika"})
# print(employees)

#! adding items : use update function

# employess = {
#     "Name": "Anamika",
#     "Age": 19
# }
# employess.update({"Address":"Sanothimi"})
# print(employess)

# employess = {
#     "Name": "Anamika",
#     "Age": 19
# }

# for x  in employess.items():
#     print(x)
#     print(type(x))

fruit1 = {
    "name":"Strawberry",

}
fruit2 = {
    "name" : "Apples"
}

fruits ={
    "fruit1":fruit1,
    "fruit2":fruit2,
}
print(fruits)
print(fruits["fruit2"]["name"])


for x, obj in fruits.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
