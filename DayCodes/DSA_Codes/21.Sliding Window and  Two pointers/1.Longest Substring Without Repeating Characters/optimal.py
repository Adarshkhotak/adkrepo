'''TC=O(N)
SC+O(N)'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = dict()
        left = 0
        right = 0
        length = 0
        n = len(s)
        while right < n:
            if s[right] in hash_map:
                left = max(hash_map[s[right]] + 1, left) #Seraching in hash_map for s[right] gives last s[right] present in hash_map
            hash_map[s[right]] = right
            length = max(length, right - left + 1)
            right += 1
        return length