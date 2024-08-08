from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        nums[:]=nums[n-k:]+nums[:n-k]
        return nums

a=Solution()
print(a.rotate([1,2,3,4,5,6,7],3))