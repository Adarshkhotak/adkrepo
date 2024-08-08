"""
Count the number of subsequences where sum=K.
Time complexity -> O(2^n)
"""

from typing import List


def backtrack(subset: List[int], index: int, total: int):
    if total == k:
        return 1
    elif total > k:
        return 0
    if index >= len(nums):
        return 0
    subset.append(nums[index])
    Sum = total + nums[index]
    left = backtrack(subset, index + 1, Sum) #return 1 or 0 -pickup
    e = subset.pop()
    Sum -= e
    right = backtrack(subset, index + 1, Sum) #return 1 or 0  -Not pickup
    return left + right #add p and np and return the no. of sebset got created


nums = [1, 2, 3]
k = 3
count = backtrack([], 0, 0)
print(count)