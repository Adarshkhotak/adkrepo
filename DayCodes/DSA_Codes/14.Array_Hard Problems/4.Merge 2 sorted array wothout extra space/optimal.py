'''TC+O(n+m) + O(nlog⁡n + mlog⁡m)
    SC=O(1)'''

from typing import *

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    n=len(a)
    m=len(b)
    left=n-1
    right=0
    while left >=0 and right < m:
        if a[left] > b[right]:
            a[left],b[right]=b[right],a[left]
        left-=1
        right+=1
    a.sort()
    b.sort()
    return a+b