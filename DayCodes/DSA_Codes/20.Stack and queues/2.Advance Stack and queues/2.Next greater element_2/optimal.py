from typing import List
'''TC=O(2N)==O(N)
SC=O(N) -> for stack worst case'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1): #to create a cycle
            while stack and stack[-1] <= nums[i % n]:  #9%5= 4==i if n=5
                stack.pop()

            if i < n:
                if stack:
                    result[i] = stack[-1]
            stack.append(nums[i % n]) 
        return result