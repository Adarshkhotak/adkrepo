'''TC + O(N**2)
   SC= O(N)-- due to hash'''
#Works for coding ninja
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        for i in range(n):
            hashset = set()   #imp
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))
                hashset.add(nums[j])

        ans = list(result)
        return ans