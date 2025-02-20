'''TC= O(NlogN)+O(N)
  SC=O(N)'''

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        ans=[]
        intervals.sort()
        for i in range(0,n):
            if len(ans)==0 or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
        return ans
            