def calculate_mean(*variables):
    temp = 0
    for i in variables:
        temp+=i
    mean = temp/len(variables)    
    return mean

def calculate_median(*variables):
    
   # sortedVariable = list(set(variables)) #! error because set doesnot support duplicate values!!!
    sortedVariable = sorted(variables)
    n= len(variables)
    
    
        # n+=1 #! siddai len nikale vai halyo ni!!
    if(n %2 ==0):
        temp =(n+1)//2
        median  = (sortedVariable[temp-1]+sortedVariable[temp])/2
    else:
        temp = n//2 
        median = sortedVariable[temp]
    return median

if __name__ == "__main__": #! yo garena vani aru files ma pani run hunxa!!

    median = calculate_median(2,23,4,5,7,8,53,3)
    print(median)

