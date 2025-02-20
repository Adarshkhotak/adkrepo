class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiouAEIOU')
        curr_vow=0
        for ch in s[:k]:
            if ch in vowels:
                curr_vow+=1
        max_vow=curr_vow
        for i in range(k,len(s)):
            if s[i] in vowels:          #check for nxt
                curr_vow+=1
            if s[i-k] in vowels:         #remove last
                curr_vow-=1
            max_vow=max(max_vow,curr_vow)
        return max_vow


        