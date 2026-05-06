# creating a function

#! creating a function

# def my_Function():
#     print("Anamika")

# my_Function()    


#! passing the parameters

# def printName(name = "Anamika"):
#     print("hello",name)


# printName("Rahul")    

# def names(person):
#     print("Name: ",person["name"])
#     print("Address: ",person["address"])

# user = {
#     "name":"Anamika",
#     "address":"Sanothimi"
# }
# names(user)


#! Return Values:


# a good function should return a value

# def calculate(a,b):
#     return (a+b)

# print(calculate(2,3))

# def handleNumber():
#     return(1,2)

# x,y = handleNumber()
# print(f'x: {x} and y: {y}')

#! position only arguments:

# add / at the end of the argument to indicate positional arguments

def myFunction(name,/):
    return name

name = "ANamika"
print(myFunction(name))

# keyword only argument

def functionName(*,name):
    print(name)
functionName(name= "Anamika")    
