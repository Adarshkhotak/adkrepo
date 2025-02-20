'''SC= O(N)
TC=O(3N)~=O(N)'''
class Solution:
    def reverseWords(self, s: str) -> str:
        rev = s.split()
        rev.reverse()
        res=" ".join(rev)
        return res