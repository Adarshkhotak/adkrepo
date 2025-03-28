
from typing import List

"""
Time complexity -> O(2 * 2N)
N is the number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def countSubArrayLessThanOrEqualToGoal(self, nums, goal):
        if goal < 0: #VVIMP step
            return 0
        count = 0
        n = len(nums)
        left = 0
        right = 0
        Sum = 0
        while right < n:
            Sum += nums[right]
            while Sum > goal:
                Sum -= nums[left]
                left += 1
            count = count + ((right - left) + 1)#-->It gives count of all subarry whose sum <= goal
            right += 1
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.countSubArrayLessThanOrEqualToGoal(nums, goal) - self.countSubArrayLessThanOrEqualToGoal(nums, goal - 1)
