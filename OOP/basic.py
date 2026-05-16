# from rich import print
# class Student:
#     x=6

# student1 = Student()
# print(student1.x)
# print(f"deleting object... ")
# del student1

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("Anamika",18)
# print(s1.name)
# print(s1.age)
# s2 = Student("Rahul",13)
# print(s2.name)


# class Dog:
#   def __init__(self,name,age):
#        self.name =name
#        self.age = age
#   def bark(self):
#     print(f'{self.name} says woof')
# d1 = Dog("Buddy",3)
# d1.bark()


       
#! The self method

# class Student:
    
#     def __init__(self,name,age,students):
#                self.name = name
#                self.age =age
#                self.students = students
#     def sayHello(self):
#             print(f'Hello {self.name}.You\'re {self.age} years old')
#     def printStudents(self):
#             for i in range(len(self.students)):
#                     print(i)        

# # students = [1,2,3,4,5]
# s1 = Student("Anamika",13,students=[1,2,3,4,5])
# s1.sayHello()
# s1.printStudents()




# class CalculateMaths:
#     def __init__(self,student_name):
#         self.student_name = student_name
#     def calculateAverage(self,scores:list):
#         return sum(scores)/len(scores)

# numbers = [2,3]
# c1 = CalculateMaths("Anamika")
# result = c1.calculateAverage(numbers)     
# print(result)


# class Invoice:
#     def __init__(self, client_name):
#         self.client_name = client_name

#     def calculate_total(self, items: dict[str, float]) -> float:
#         # items = {"Web Design": 500.0, "Hosting": 120.0}
#         return sum(items.values())

#     def print_summary(self, items: dict[str, float]):
#         for service, price in items.items():
#             print(f"  {service}: ${price:.2f}")
#         print(f"  TOTAL: ${self.calculate_total(items):.2f}")

# # Usage
# invoice = Invoice("Acme Corp")
# services = {
#     "Web Design": 500.0,
#     "SEO Optimization": 300.0,
#     "Hosting": 120.0
# }
# invoice.print_summary(services)


"""Create a class called Car
Add an __init__ method with a brand parameter, and store it as a property
Add a method called show that prints the brand
Create an object c1 of the Car class with brand "Ford"
Call the show method on c1"""

# class Car:
#     def __init__(self,brand):
#         self.brand = brand
#     def show(self):
#         print(self.brand)

# c1 = Car("Ford")
# c1.show()        

# c1.brand = "Toyota"
# c1.show()


# class Person:
#   lastname = ""

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")

# Person.lastname = "Refsnes"

# print(p1.lastname)
# print(p2.lastname)


# class CarBrands:
#     def __init__(self,brand):
#         self.brand = brand

# c1 = CarBrands("Toyota")
# c1.model = 2021
# print(c1.model)    
"""Inside the editor, complete the following steps:
Create a class Student with an __init__ that takes name and grade, and stores them as properties
Create an object s1 with name "Anna" and grade "A"
Print the grade of s1
Change the grade of s1 to "B"
Print the updated grade"""


# class Student:
#     def __init__(self,name,grade,age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#     def happyBirthday(self):
#         self.age+=1
#         print(f'Happy {self.age}th birthday')

# s1 = Student("Anamika",12,20)
# s1.happyBirthday()
# s1.happyBirthday()            


# class Person:
#     def __init__(self,name):
#         self.name = name
# p1 = Person("Anamika")
# print(p1)  #! this returs the object location!


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
    
# p1 = Person("Anamika",23)
# print(p1)

from rich import print
class Interests:
    def __init__(self,name):
            self.name = name
            self.interest = []

    def addInterest(self,interest):
          self.interest.append(interest)
          print(f"[bold green]{interest} added[/bold green]")  
    def removeInterest(self):
          self.interest.pop(len(self.interest)-1)
          print(f"[bold red]One Item of interest removed[/bold red]")       
    def printInterests(self):
          print(self.interest)
p1 = Interests("Anamika")
p1.addInterest("Cricekct")
p1.addInterest("Skate")
p1.removeInterest()
p1.printInterests()


"""Create a class called Rectangle
Add an __init__ method with width and height, and store them as properties
Add a method called area that returns the width multiplied by the height
Create an object r1 with width 5 and height 3
Print the area of r1"""

class Rectange:
    def __init__(self,width,height):
            self.width = width
            self.height = height
    def Area(self):
          return (self.width*self.height)
    
r1 = Rectange(5,3)
print(r1.Area())    