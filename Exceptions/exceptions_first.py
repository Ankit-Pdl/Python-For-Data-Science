from rich import print

# try:
#     print(x)
# except:
#     print("[bold red]x is not defined[/bold red]")    


# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#  for i in range(5):
#   print(5/i)
# except:
#   print("Divide by zero error")  
    
for i in range(10):
    if i ==5:
        raise ValueError("I is 5")
    print(i)    