from typing import List
"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=0
        return max(max_count,count) #we can't return only max_count coz if we don't get '0' at end gives different result
    
a=Solution()
print(a.findMaxConsecutiveOnes([1,1,0,1,1,1]))