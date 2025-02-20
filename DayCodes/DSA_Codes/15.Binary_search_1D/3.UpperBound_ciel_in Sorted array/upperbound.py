from typing import List
"""
Time complexity -> O(logn)
n is number of elements in nums

Space complexity -> O(1)
"""
#pper bound ar[i]>target
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        UB = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                UB = mid
                high = mid - 1
            else:
                low = mid + 1
        return UB
#Solution of floor&ceil (upperbound)
'''
"""
Time complexity -> O(logn)
n is number of elements in nums

Space complexity -> O(1)
"""
def getFloorAndCeil(a, n, x):
    floor = -1
    ceil = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return x, x
        elif a[mid] > x:
            ceil = a[mid]#imp a[mid] asked value not index
            high = mid - 1
        else:
            floor = a[mid]
            low = mid + 1
    return floor, ceil'''