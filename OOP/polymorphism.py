# same function can have different objectives!

# class Dog:
#     def speak(self):
#         print("Bhow")

# class Cat:
#     def speak(self):
#         print("meow")


# class Lion:
#     def speak(self):
#         print("Roar")

# dog = Dog()
# dog.speak()
# cat = Cat()
# cat.speak()
# lion = Lion()
# lion.speak()                

#! inheritance with polymorphism

# class Vehicle:
#     def __init__(self,name):
#         self.name = name
#     def func(self):
#         print("Run")

# class Car(Vehicle):
#     pass
# class Plane(Vehicle):
#     def func(self):
#         print("FLy")
# class Horse(Vehicle):
#     def func(self):
#         print("Tukduk Tukduk")

# c1 = Car("Ford")
# p1 = Plane("Boeng")
# h1= Horse("Kali")

# for x in (c1,p1,h1):
#     x.func()                


#* practice questions:
"""Inside the editor, complete the following steps:
Create a class Cat with a method sound that prints "Meow"
Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
Create objects c1 = Cat() and f1 = Fox()
Call sound() on both objects"""

class Cat:
    def sound(self):
        print("Meow")

class Fox:
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow!")

c1 = Cat()
f1 = Fox()
for x in (c1,f1):
    x.sound()        