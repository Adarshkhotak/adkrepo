from typing import List
def gensubseq(subset:List[int],index):
    if index >=len(nums):
        res.append(subset.copy())
        return
    subset.append(nums[index])
    gensubseq(subset,index+1)
    subset.pop()
    gensubseq(subset,index+1)
    
   


res=[]
nums=[3,1,2]
gensubseq([],0)
print(res)