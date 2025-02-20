from typing import List
def roseGarden(arr: List[int], r: int, b: int):
    def possiblebq(bloomDay,m,k,day):
            total_bqt=0
            count=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=day:
                    count+=1
                    if count==k:
                        count=0
                        total_bqt+=1
                else:
                    count=0
            return total_bqt>=m
    
    for i in range(min(arr),max(arr)+1):
        if possiblebq(arr,b,r,i):
            return i
    return -1