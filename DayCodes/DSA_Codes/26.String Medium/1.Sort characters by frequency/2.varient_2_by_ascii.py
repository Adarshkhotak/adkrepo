'''TC= O(N)+O(n log n)+O(N)
    SC=O(N)'''

class Solution(object):
    def frequencySort(self, s):
        res=""
        hash_map=dict()
        for ch in s:
            hash_map[ch]=hash_map.get(ch,0)+1
        
        sorted_ch= sorted(hash_map.items(), key=lambda x:(-x[1],x[0])) #if x[1](- cause sort desc) is same then sort by x[0](character) by asci value
        for ch , freq in sorted_ch:
            res=res+ch * freq
        return res