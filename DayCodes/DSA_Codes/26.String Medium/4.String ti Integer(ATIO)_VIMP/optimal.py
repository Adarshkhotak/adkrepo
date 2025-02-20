'''TC=O(N)
    SC=O(1)'''
class Solution(object):
    def myAtoi(self, s):
        max_int=2**31 - 1
        min_int=-2**31
        sign=1
        n=len(s)
        res=0
        idx=0
        while idx < n and s[idx]==" ":
            idx+=1
        
        if idx < n:
            if s[idx]=="+":
                sign=1
                idx+=1
            elif s[idx]=="-":
                sign=-1
                idx+=1
        
        while idx < n and s[idx].isdigit(): #chk string character is num or not
            digit=int(s[idx])
            res=(res*10)+ digit
            idx+=1

            if res > max_int:
                if sign==1:
                    return max_int
                else:
                    return min_int
        return res*sign