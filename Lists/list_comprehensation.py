# advanced shorter syntax if you want to create a new list


even_Numbers = [x for x in range(10) if x %2 ==0]
print(even_Numbers)

square = [x**2 for x in even_Numbers ]
print(square)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

c_fruit = [x for x in fruits if "c" in x]
print(c_fruit)