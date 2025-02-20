"""
Time complexity -> O(n^2)
n is number of elements in nums

Space complexity -> O(1)
"""
from typing import List
def longestSubarrayWithSumK(a: List[int], k: int) -> int:
    n=len(a)
    max_len=0
    for i in range(0,n):
        sum=0
        for j in range(i,n):
            sum=sum+a[j]
            if sum==k:
                max_len=max(max_len,j-i+1)
    
    return max_len

a=longestSubarrayWithSumK([1,2,0,3,4,5,4,3,34,54,32,21,334,12,1],0)
print(a)