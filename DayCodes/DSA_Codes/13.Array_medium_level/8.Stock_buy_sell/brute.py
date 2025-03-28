from typing import List
"""
Time complexity -> O(n^2)
n is number of elements in nums

Space complexity -> O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    maxProfit = max(prices[j] - prices[i], maxProfit)

        return maxProfit