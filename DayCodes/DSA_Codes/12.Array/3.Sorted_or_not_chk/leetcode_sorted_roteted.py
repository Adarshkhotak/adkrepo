from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        breakpoint = 0
        n = len(nums)
        for i in range(0,n):  #n (insted of n-1) coz copmare last with first
            if nums[i]>nums[(i+1)%n]: #by this we compare last with first to check breaking point
                breakpoint+=1

                if breakpoint>1:
                    return False
        return True 
a=Solution()        
print(a.check([3,4,5,1,2]))