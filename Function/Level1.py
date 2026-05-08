# *args and kargs

#! use *args if you don't know the number of arguments going to be use in the function

# def college(*students):
#     print("The smartest student is " + students[3] )


# college("rahul","anamika","ankit","sohil")   

# def sumTotal(*args):
#     total = 0
#     for num in args:
#         total += num
#     print(total)

# sumTotal(1,2,3,4)


#! better way of doing the same work:

# def sum_Total(*args):
#     return sum(args)

# print(sum_Total(1,2,3,4,5,6))

#! problem to find the maximum value:

# def find_Maximum(*numbers):
#     if len(numbers) == 0:
#         return 
#     maxNumber = numbers[0]
#     for i in numbers:
#         if i>maxNumber:
#             maxNumber = i
#     return maxNumber

# maximum = find_Maximum(12,3,4,6,344)
# print(maximum)

#!Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

# This way, the function will receive a dictionary of arguments and can access the items accordingly:

# def names(**names):
#     print("good student of nist college is: "+ names["last"])

# names(first= "Ankit",last = "Poudel")
