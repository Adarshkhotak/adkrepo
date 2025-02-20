"""
Time complexity -> O(logN)
N is the number

Space complexity -> O(1)
"""


def floorSqrt(n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid**2==n:
            return mid
        if mid * mid <= n: #or mid**2
            low = mid + 1
        else:
            high = mid - 1
    return high


n = int(input())
print(floorSqrt(n))

#OR
'''
def floorSqrt(n):
      l=0
      h=n
      while l<=h:
         m=(l+h)//2
         if m**2 > n:
            h=m-1
         else:
            l=m+1
      return h'''