"""
Print all the subsequences where sum=K.
Generate every one of them

Time complexity -> O(2^n)
"""

from typing import List


def backtrack(subset: List[int], index: int, total: int):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    if index >= len(nums):
        return
    subset.append(nums[index])
    Sum = total + nums[index]
    backtrack(subset, index + 1, Sum)
    e = subset.pop()
    Sum -= e
    backtrack(subset, index + 1, Sum)


result = []  #we are changing in result don' need to return anything
nums = [3,1,2]
k = 3
backtrack([], 0, 0)
print(result)