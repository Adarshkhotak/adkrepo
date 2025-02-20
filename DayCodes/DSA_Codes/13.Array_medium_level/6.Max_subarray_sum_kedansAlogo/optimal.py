from typing import List
"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""
# Also known as Kadane’s Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        Sum = 0
        n = len(nums)
        for i in range(n):
            Sum += nums[i]

            if Sum > maxi:
                maxi = Sum

            # If sum is -ve make it to 0 kadanse algi
            if Sum < 0:
                Sum = 0
        # To consider the sum of the empty subarray
        # uncomment the following check:
        # if maxi < 0: maxi = 0
        return maxi
    
'''#Coding ninja for different condition
def maxSubarraySum(arr, n) :
    max_sum=float("-inf")
    sum=0
    for i in range(0,n):
        sum=sum+arr[i]

        if sum>max_sum:
            max_sum=sum
        if sum<0:
            sum=0

        if max_sum<0:
            return 0
    return max_sum'''