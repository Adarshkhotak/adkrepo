from typing import List

"""
Time Complexity = O(n)
Space Complexity = O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k=k% n  # Handle cases where k > n

        reverse(0, n - 1)  # Reverse the entire array
        reverse(n-k,n-1)  # Reverse the last k elements
        reverse(0, n-k-1)  # Reverse the remaining starting elements

        return nums

a=Solution()
print(a.rotate([1,2,3,4,5,6,7],3))