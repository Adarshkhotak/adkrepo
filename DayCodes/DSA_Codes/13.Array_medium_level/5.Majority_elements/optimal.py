'''
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
'''

# Also known as Moore’s Voting Algorithm
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:   #change the candidate
                candidate = nums[i]
                count = 1 #--> imp to add this
        return candidate