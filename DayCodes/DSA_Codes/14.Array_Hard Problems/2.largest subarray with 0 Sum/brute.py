'''TC=O(N**2)
   sc=O(1)'''

from typing import *

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    n=len(arr)
    max_l=0
    for i in range(0,n):
        sum=0
        for j in range(i,n):
            sum=sum+arr[j]
            
            if sum==0:
                ln= j-i+1
                max_l=max(max_l,ln)
    return max_l