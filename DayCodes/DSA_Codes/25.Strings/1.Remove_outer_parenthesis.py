'''TC=O(N)
SC=O(1)'''
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        count=0
        for ch in s :
            if ch =="(":
                count+=1
                if count > 1 :
                    res=res+ch
            else:
                count-=1
                if count > 0:
                    res+=ch

        return res
        