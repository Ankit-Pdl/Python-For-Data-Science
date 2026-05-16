
#! Encapsulation is about making data private,protexted or public


# class Parent:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

# p1 =Parent("Anmaika",18)
# print(p1.name)
# print(p1.age)        

# to access the private values, we need to pass it to  a functions

# class Parent:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def display(self):
#         return self.__age 
#     def modify(self,age):
#         self.__age = age
# p1 = Parent("anamika",15)
# print(p1.name)
# print(p1.display()) 
# p1.modify(144)
# print(p1.display())      

# #! program to illustrate protected property

# class Parent:
#     def __init__(self,name,age):
#         self.name = name
#         self._age = age

# p1 = Parent("Ankit",31)
# print(p1._age) #! don't access data like this!



"""Create a class ScoreBoard
Add an __init__ with a score parameter and store it as a private attribute
Add a method called get_score that returns the private score
Create an object s1 with a score of 0
Print the score of s1"""

class ScoreBoard:
    def __init__(self,score):
        self.__score = score
    def get_score(self):
        return self.__score

s1 = ScoreBoard(0)
print(s1.get_score())    