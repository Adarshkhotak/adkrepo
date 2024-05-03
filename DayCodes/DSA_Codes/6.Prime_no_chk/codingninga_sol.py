def checkPrime(n:int):
    if n == 1:
        return 'NO'
    for i in range(2,int(n**0.5)+1): #or (2,sqrt(n)+1)
        if n%i==0:
            return 'NO'
    return 'YES'

n=int(input())
print(checkPrime(n))