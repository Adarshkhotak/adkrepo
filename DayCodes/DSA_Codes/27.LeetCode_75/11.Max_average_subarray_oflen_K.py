from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        curr_sum=sum(nums[:k])
        max_sum=curr_sum
        for i in range(k,n):  #imp k
            curr_sum+= nums[i] - nums[i-k]
            max_sum=max(max_sum,curr_sum)
        
        return max_sum/k