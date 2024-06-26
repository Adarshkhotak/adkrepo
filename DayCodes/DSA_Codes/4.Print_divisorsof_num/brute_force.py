"""
Brute Force
TC - O(n), where n is the number
SC - O(d), where d is the number of divisors of the input integer n
"""

from typing import List

def printDivisors(n: int) -> List[int]:
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res

a=printDivisors(20)
print(a)

#it has less TC than optimal one bcoz it sorts during appending only