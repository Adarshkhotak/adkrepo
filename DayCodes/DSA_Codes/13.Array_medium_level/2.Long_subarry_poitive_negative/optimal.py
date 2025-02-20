from sys import *
from collections import *
from math import *
from typing import List
"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""
def getLongestSubarray(nums: List[int], k: int) -> int:
    n=len(nums)
    sum_dict=dict()
    max_len=0
    sum=0
    for i in range(0,n):
        sum=sum+nums[i]
        if sum==k:
            max_len=i+1
        
        rem=sum-k
        if rem in sum_dict:
            ln=i-sum_dict[rem]
            max_len=max(max_len,ln)
        
        if sum not in sum_dict:
            sum_dict[sum]=i
    return max_len
