from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True
    
a=Solution()
print(a.check([3,4,5,1,2]))