class Solution:
    def reverse(self, x: int) -> int:
        reverse=0
        is_negative=False
        if x<0:
            is_negative=True
            x=x*-1
        while x>0:
            last_digit=x%10
            reverse=(reverse*10)+last_digit
            x//10
        return reverse
        '''if is_negative:
            reverse=reverse*-1
        if reverse <(-2**31) or reverse>(2**31 -1):
            return 0
        return reverse'''
    
a=Solution()
re=a.reverse(122)
print(re)