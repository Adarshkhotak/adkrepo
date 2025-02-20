from typing import List
"""
Time complexity -> O(logn)
n is number of elements in nums

Space complexity -> O(1)
"""
#Lower bound ar[i]>=target
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        LB = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                LB = mid
                high = mid - 1
            else:
                low = mid + 1
        return LB
    
#Solutuion for geeksforgeeks -Floor in sorted array they want arr[i]<=target
'''
class Solution:

    def findFloor(self,A,N,X):
        l=0
        h=N-1
        pos=-1
        while l<=h:
            mid=(l+h)//2
            if A[mid]<=X: # Just condition changed
                pos=mid
                l=mid+1 #IMP also this one
            else:
                h=mid-1
        return pos'''