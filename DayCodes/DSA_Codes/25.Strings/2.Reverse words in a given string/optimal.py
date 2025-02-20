'''TC=O(N)
  SC=O(N)'''
class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        i=len(s)-1
        while i >=0:
            if s[i]==" ":
                i-=1
                continue
            
            word=""
            while i >=0 and s[i]!=" ":
                word=s[i]+word  #s[i] first bcoz to add char in front of word
                i-=1
            
            if res!="":  #to add space btw words
                res+=" "
            res=res+word

        return res    
        