#TC=O(N),SC=O(N)
def singleNonDuplicate(arr):
    my_dict=dict()
    for i in range(0,len(arr)):
        my_dict[arr[i]]=my_dict.get(arr[i],0)+1
    for k,v in my_dict.items():
        if v==1:
            return k
        
#OR
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-2]!=nums[n-1]:
            return nums[n-1]
        for i in range(1,n-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]