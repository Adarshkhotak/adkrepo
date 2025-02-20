from typing import List
'''TC=O(N)
    SC=O(1)'''
def findMissingRepeatingNumbers(a: List[int]) -> List[int]:
    n=len(a)
    sn=(n*(n+1))//2
    s2n=(n*(n+1)*(2*n+1))//6
    sm=0
    sm2=0
    for num in a:
        sm+= num
        sm2+= num**2
    
    val1=sm-sn  #x-y
    val2=sm2-s2n  #x**2-y**2

    val2=val2//val1  #--> x+y
    x=(val1+val2)//2  #--> (x-y+x+y)==>2x/2==x
    y=x-val1
    return [x,y]
