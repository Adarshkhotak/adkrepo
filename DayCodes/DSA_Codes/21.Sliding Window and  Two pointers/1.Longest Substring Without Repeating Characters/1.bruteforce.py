'''TC=O(N**2)
SC=O(N)'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxans = 0
        for i in range(len(s)):
            set = {}
            for j in range(i, len(s)):
                if s[j] in set:
                    break
                maxans = max(maxans, j - i + 1)
                set[s[j]] = 1
        return maxans
#OR-BY using set()

def uniqueSubstrings(input ) :
    s=input
    if len(s)==0:
        return 0
    n=len(s)
    ans=0
    for i in range(0,n):
        my_set=set()
        for j in range(i,n):
            if s[j] in my_set:
                break
            my_set.add(s[j])
            ans=max(ans, j-i+1)
    return ans