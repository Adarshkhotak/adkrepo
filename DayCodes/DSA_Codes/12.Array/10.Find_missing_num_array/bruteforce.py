from typing import List
"""
Time complexity -> O(n^2)
n is number of elements in nums

Space complexity -> O(1)
"""
def missingNumber( nums: List[int]) -> int:
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
            
print(missingNumber([3,2,1,6,0]))

#To find multipal numbers and return a list.So SC=O(N)
def missingNumber( nums: List[int]) -> int:
        res=[]
        for i in range(0,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res
            
print(missingNumber([3,2,1,6,0]))