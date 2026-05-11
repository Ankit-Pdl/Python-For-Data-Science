

# #! decorators provides extra feature to a function without actually changing its code.!

# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# # @changecase
# # def myFunction():
# #     return "Hello world"
# #! yo @changecase lai disect garne ho bhaney::

# def myFunction():
#     return "Hello world"

# myFunction = changecase(myFunction)
# print(myFunction())


def outerFunction(func):
    def innerFunction():
        return func().capitalize()
    return innerFunction

@outerFunction
def tempFunction():
    return "anamika is a good girl!"

print(tempFunction())