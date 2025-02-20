'''TC=O(M*N)
SC=O(1)'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        base=strs[0]
        for i in range(0,len(base)):
            for word in strs[1:]:
                if i==len(word) or base[i]!= word[i]:
                    return res
            res+=base[i] 
        return res       #edge case if input strs is empty 