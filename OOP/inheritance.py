# logically C++ ma padheko jastai ho same! just learn the syntax okay

class Parent:
    def __init__(self,name="anamika"):
        self.name = name

class Child(Parent):
    def __init__(self,name):
        self.name = name
        super().__init__(name)
    

c1 = Child("Ankit")
print(c1.name)