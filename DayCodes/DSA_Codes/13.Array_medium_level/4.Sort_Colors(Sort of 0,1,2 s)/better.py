from os import *
from sys import *
from collections import *
from math import *
"""
Time complexity -> O(2N) -> O(N)
n is number of elements in nums

Space complexity -> O(1)
"""

def sortArray(arr, n):
	cnt0=0
	cnt1=0
	cnt2=0
	for i in range(0,len(arr)):
		if arr[i]==0:
			cnt0+=1
		if arr[i]==1:
			cnt1+=1
		if arr[i]==2:
			cnt2+=1
	print(cnt0)
	for i in range(0,cnt0):
		arr[i]=0
	for i in range(cnt0,cnt1+cnt0): #IMP ranges
		arr[i]=1
	for i in range(cnt0+cnt1,cnt0+cnt1+cnt2):
		arr[i]=2

	return arr

print(sortArray( [2, 2, 2, 2, 0, 0, 1, 0],8))