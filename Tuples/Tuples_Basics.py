# unmutable data structure to store a collection of datas

myTuple = ("Anamika","Unsaaa","Rahul")
#print(myTuple(0))   #!error occurs
# ? correct way:

print(myTuple[0])

print(len(myTuple))

# //! tuple with only one data needs an extra comma at the end else python doesn't recognizes it

students = ("Ankit")
print(type(students)) # identified as strings!!!

myStudents = ("Students",)
print(type(myStudents))

# * Tuples can hold multiple data types like in Lists

tuple1 = ("Ankit",True,24)

names = "Ankit", " Rahul" # also a tuple
print(names)
print(type(names))

