from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n

        prfix=1
        for i in range(n):
            res[i]=prfix
            prfix=prfix*nums[i]

        sufix=1
        for i in range(n-1,-1,-1):
            res[i]=res[i]*sufix
            sufix=sufix*nums[i]

        return res 