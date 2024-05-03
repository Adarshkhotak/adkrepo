def sumOfAllDivisors(n:int):
    sum=0
    for i in range(1,n+1):
        sum=sum+(n//i)*i
    return sum
    
a=sumOfAllDivisors(5)
print(a)