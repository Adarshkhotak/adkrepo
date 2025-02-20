from typing import *
"""
Time complexity -> O(N)
N is number of elements in nums

Space complexity -> O(1)
"""
def superiorElements(a : List[int]) -> List[int]:
    ar=[]
    n=len(a)
    max_no=float("-inf")
    for i in range(n-1,-1,-1):
        spe=max(max_no,a[i])

        if spe>max_no:
            ar.append(spe)
            max_no=spe
    return ar

print(superiorElements( [1,5, 2, 3, 2,4]))

#OR
from typing import *

def superiorElements(a : List[int]) -> List[int]:
    ar=[]
    n=len(a)
    spe=0
    for i in range(n-1,-1,-1):
        num_ele=a[i]

        if num_ele > spe:
            ar.append(num_ele)
            spe=num_ele
    return ar