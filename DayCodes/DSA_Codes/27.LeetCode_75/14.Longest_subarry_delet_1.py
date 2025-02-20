from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero=0
        l=0
        r=0
        max_len=0
        while r <len(nums):
            if nums[r]==0:
                zero+=1
            while zero > 1:
                if nums[l]==0:
                    zero-=1
                l+=1
            max_len=max(max_len,r-l)  #not +1 coz the one element is deleted
            r+=1
        return max_len
        