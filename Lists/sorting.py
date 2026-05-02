# sorting:

# alpahbetic sorting 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits.sort()
fruits.sort(reverse=True)
print(fruits)

numbers = [1,2,5,67,47,53,268,22,68,3245,8653,22]

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)