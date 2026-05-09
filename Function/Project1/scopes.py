
# age = 0 #* global variable


# def myFunction():
#     x = int(input("Enter a number: ")) #! x is the local variable
#     age = x**3
#     return age

# result = myFunction()
# print(result)



#! non local variable

#! used in nested functions

def calcSum():
    x =5
    def calcMul():
        nonlocal x # this variable is available to the parent function toooo!!
        return x*2
    x= calcMul()
    return x 

print(calcSum())
