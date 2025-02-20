#Brute--exceeding time limit
from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        for spell in spells:
            count=0
            left=0
            right=len(potions)-1
            while left <= right:
                if spell * potions[left] >= success:
                    count=count + (right-left +1)
                    break
                left+=1
            res.append(count)
        return res
        