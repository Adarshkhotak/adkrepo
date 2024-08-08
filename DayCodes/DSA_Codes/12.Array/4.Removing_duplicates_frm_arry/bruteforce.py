from typing import List

"""
Time complexity = O(n) where n is the number of elements in list
We are looping two different times, so it will be O(n) + O(n).
Which equals tos O(n)

Space complexity = O(n), suppose all numbers are unique, it will take same length as list
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_dict = dict()
        for i in nums:
            my_dict[i] = 0

        j = 0
        for key in my_dict: #list converted to dict which don't contain any duplicate key
            nums[j]=key  #Change in arr in place
            j += 1  #count the keys(alway unique)
        return j  #return the len after removing duplicates
    
a=Solution()
print(a.removeDuplicates([1, 2, 2,4, 2, 3]))