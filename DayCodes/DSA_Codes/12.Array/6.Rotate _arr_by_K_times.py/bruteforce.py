from typing import List

"""
Time complexity = O(r*n), where r is number of rotations
and n is number of elements in the array

Space complexity = O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Becuase if k = 8 and length = 7, means  i.e k% len(nums)
        # we should only rotate 1 time instead of 8 times
        rotations = k % len(nums)

        for _ in range(rotations):
            last = nums.pop()#empty means last
            nums.insert(0, last)
        return nums
    
a=Solution()
print(a.rotate([1,2,3,4,5,6,7],3))