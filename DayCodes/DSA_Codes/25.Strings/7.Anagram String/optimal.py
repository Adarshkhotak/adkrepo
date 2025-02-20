'''TC=O(N)
SC=O(26) -- num of alphabates'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        freq=dict()
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        
        for ch in t :
            if ch not in freq:
                return False
            else:
                if freq[ch]==0:
                    return False
                else:
                    freq[ch]-=1
        return True

        
        