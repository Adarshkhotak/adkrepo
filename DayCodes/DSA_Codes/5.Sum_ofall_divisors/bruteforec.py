def sumOfAllDivision(n:int):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i +1):
            if i%j==0:
                sum=sum+j

    return sum
a=sumOfAllDivision(5)
print(a)