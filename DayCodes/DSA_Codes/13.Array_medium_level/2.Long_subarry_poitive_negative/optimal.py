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
    start, end= -1,-1
    for i in range(0,n):
        sum=sum+nums[i]
        if sum==k:
            max_len=i+1
            start=0
            end=i
        
        rem=sum-k
        if rem in sum_dict:
            ln=i-sum_dict[rem]
            if ln > max_len:
                max_len=ln
                strat= sum_dict[rem]+1
                end=i
        
        if sum not in sum_dict:
            sum_dict[sum]=i
    if start==-1 and end ==-1:
        return []
    return max_len , nums[start : end+=1]
