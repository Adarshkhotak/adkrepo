'''TC=O(N**2)
SC=O(N)'''
def longestSubSeg(arr, n, k):
    res=0
    for i in range(0,n):
        zr=0    #zr needs to be initialised here only coz for every i we count zeros
        for j in range(i,n):
            if arr[j]==0:
                zr+=1
            
            if zr > k:
                break
            
            res=max(res,j-i+1)
    return res

#OR
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        n = len(nums)
        for i in range(n):
            zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1
                if zeros <= k:
                    length = j - i + 1
                    max_length = max(max_length, length)
                else:
                    break
        return max_length