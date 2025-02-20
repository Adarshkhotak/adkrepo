from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero=0
        r=0
        l=0
        res=0
        while r < len(nums):
            if nums[r]==0:
                zero+=1
            if zero > k:
                if nums[l]==0:
                    zero-=1
                l+=1
            if zero <= k:
                res=max(res,r-l+1)
            r+=1 
        return res


        