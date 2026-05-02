# list1= [1,2,4,56,45]
# list2 =list1
# print(list2) # changes made in list1 will affect the changes made in list 2



num1 = [1,2,3]
# num2 = num1
# print(num2)
# num1.append(5)
# print(num2)  # danger zone

# better way:
# num2 = list(num1)
# print(num2)
# num1.append(45)
# print(num1)
# print(num2)


# joining two lists:

list1 = [1,2,3]
list2=[4,5,6]
list3 = list2+list1
list3.sort()
print(list3)