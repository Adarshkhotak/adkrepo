from typing import List

def twoSum( nums: List[int], target: int) -> List[int]:
        sum_dict=dict()
        for i in range(0,len(nums)):
            rem=target-nums[i]
            if rem in sum_dict:
                 pos=[sum_dict[rem],i]
            if nums[i] not in sum_dict:
                sum_dict[nums[i]]=i
        return pos
#Below is good
"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n) same for above also coz returning pos only
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict=dict()
        for i in range(0,len(nums)):
            rem=target-nums[i]
            if rem in sum_dict:
                return [nums[sum_dict[rem]],nums[i]]
            sum_dict[nums[i]]=i
            
            
a=Solution()            
print(a.twoSum([3,2,4],6))