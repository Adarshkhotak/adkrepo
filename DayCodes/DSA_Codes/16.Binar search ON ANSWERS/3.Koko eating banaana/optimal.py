import math
from typing import List
"""
Time complexity -> O(N * log(max(piles)))

Space complexity -> O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_hours(piles,hourly_rate):
            total=0
            for i in range(len(piles)):
                total=total+math.ceil(piles[i]/hourly_rate) 
            return total
 
        low=1
        high=max(piles)
        ans=-1
        while low<=high:
            m=(low+high)//2
            th=total_hours(piles,m)
            if th<=h:
                ans=m
                high=m-1
            else:
                low=m+1
        return ans
a=Solution()
print(a.minEatingSpeed([3,6,7,11],8))