from math import sqrt
def checkPrime(n:int):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1): #or (2,sqrt(n)+1)
        if n%i==0:
            return False
    return True

a=checkPrime(23)
print(a)