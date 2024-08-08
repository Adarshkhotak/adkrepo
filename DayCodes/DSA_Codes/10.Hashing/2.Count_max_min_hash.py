from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    #n=len(v) we can't solve by list the hv nit given the condition like 0 to m num only
    my_dict={}
    for i in v:
        my_dict[i]=my_dict.get(i,0)+1

    minFreq = float('inf') #-->
    minElement = float('inf')
    maxFreq = float('-inf')
    maxElement = float('inf')

    for key,value in my_dict.items():
        if value > maxFreq or value==maxFreq and key < maxElement:#key< small coz they want smallent elment
            maxFreq=value
            maxElement=key
        
        if value < minFreq or value==minFreq and key < minElement:
            minFreq=value
            minElement=key

    return [maxElement,minElement]

print(getFrequencies([1, -3, 1, 9, 2, 7]))