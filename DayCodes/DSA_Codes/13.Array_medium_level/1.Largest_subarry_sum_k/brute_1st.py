"""
Time complexity -> O(n^3)
n is number of elements in nums

Space complexity -> O(1)
"""
from typing import List
def longestSubarrayWithSumK(a: List[int], k: int) -> int:
    n=len(a)
    max_len=0
    for i in range(0,n):
        for j in range(i,n):
            sum=0
            for e in range(i,j+1):
                sum=sum+a[e]
            if sum==k:
                max_len=max(max_len,j-i+1)
            if sum>k:
                break   #break nahi kiya to sum='0' nahi hoga
    return max_len

print(longestSubarrayWithSumK( [1, 2, 3, 1, 1, 1, 1],6))