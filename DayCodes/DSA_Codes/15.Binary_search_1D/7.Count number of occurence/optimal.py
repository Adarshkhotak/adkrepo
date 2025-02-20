"""
Time complexity -> O(2 * logN) -> O(logN)
N is number of elements in nums

Space complexity -> O(1)
"""

from typing import List
def count(arr:List [int], n: int, target: int) -> int:
    def loweBound(arr, n, target):
        ind = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ind = mid
                high = mid - 1
            else:
                low = mid + 1
        return ind

    def upperBound(arr, n, target):
        ind = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                ind = mid
                high = mid - 1
            else:
                low = mid + 1
        return ind

    return upperBound(arr, n, target) - loweBound(arr, n, target)

#in Class solution
'''
class Solution:

	def count(self,arr, n, x):
		def lowerbound(self,arr,n,x):
		    l=0
		    h=n-1
		    ind=n
		    while l<=h:
		        m=(l+h)//2
		        if arr[m]>=x:
		            ind=m
		            h=m-1
		        else:
		            l=m+1
		    return ind
		def upperbound(self,arr,n,x):
		    l=0
		    h=n-1
		    ind=n
		    while l<=h:
		        m=(l+h)//2
		        if arr[m]>x:
		            ind=m
		            h=m-1
		        else:
		            l=m+1
		    return ind
	
    	return upperbound(self,arr,n,x) - lowerbound(self,arr,n,x)
'''
