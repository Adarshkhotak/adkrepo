from typing import List
def maxSubArray(nums: List[int]) -> int:
        max_sum=float("-inf")
        sum=0
        start=0
        for i in range(0,len(nums)):
            sum=sum+nums[i]
            
            if sum>max_sum:
                end=i+1
                max_sum=sum
            if sum<0:
                start=i+1
                sum=0
        return nums[start:end],max_sum
        


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
