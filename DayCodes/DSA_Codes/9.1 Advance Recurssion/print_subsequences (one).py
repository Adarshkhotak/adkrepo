"""
Print all the subsequences where sum=K.
Generate only 1

Time complexity -> O(2^n)
"""

from typing import List


def backtrack(subset: List[int], index: int, total: int):
    if total == k:
        result.append(subset.copy())
        return True
    if index >= len(nums):
        return False
    subset.append(nums[index])
    Sum = total + nums[index]
    pick=backtrack(subset, index + 1, Sum) #this func is give True whin u get sum==k at 1 point.
    if pick==True: #when we get subset with k it end the this func
        return True
    e = subset.pop()
    Sum -= e
    return backtrack(subset, index + 1, Sum)


result = []
nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]
k = 8
backtrack([], 0, 0)
print(result)