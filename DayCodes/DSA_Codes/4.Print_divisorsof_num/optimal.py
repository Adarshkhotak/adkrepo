"""
Brute Force
TC - O(sqrt(n) + sqrt(n)*log(sqrt(n))), where n is the number
SC - O(sqrt(n)), where n is the number
"""
from math import sqrt
from typing import List


def printDivisors(n: int) -> List[int]:
    result = []
    for i in range(1, (int(n**0.5)) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)

    result.sort()  #It is good optimal solu if sorting is not required
    return result