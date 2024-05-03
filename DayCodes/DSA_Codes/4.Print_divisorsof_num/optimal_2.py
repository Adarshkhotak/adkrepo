
# TC - O(sqrt(n))
# SC - O(sqrt(n))
from math import sqrt
from typing import List
def printDivisors_1(n: int) -> List:
    divisorLst: List = []
    i = 1
    while i * i < n:
        if n % i == 0:
            divisorLst.append(i)
        i += 1
    for i in range(int(sqrt(n)), 0, -1):
        if n % i == 0:
            divisorLst.append(n // i)
    return divisorLst
a=printDivisors_1(100)
print(a)