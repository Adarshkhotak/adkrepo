"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""
from typing import List
def longestSubarrayWithSumK(a: List[int], k: int) -> int:
    sum=0
    max_len=0
    sum_dict=dict()
    for i in range(0,len(a)):
        sum=sum+a[i]
        if sum==k:
            max_len=i+1
        
        rem=sum-k #VIMP  sum-k not the k-sum
        if rem in sum_dict:
            ln=i-sum_dict[rem]
            max_len=max(max_len,ln)

        if sum not in sum_dict:  #IMP here SUM not the rem
            sum_dict[sum]= i
            
    return max_len