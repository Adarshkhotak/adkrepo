'''TC=O(N)
  SC= O(2N)'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        map_s_t={} #s to t
        map_t_s={}  # t to s
        for i in range(0,len(s)):
            chr_s=s[i]
            chr_t=t[i]

            if chr_s in map_s_t :
                if map_s_t[chr_s]!= chr_t:
                    return False
            else:
                map_s_t[chr_s]=chr_t
            
            if chr_t in map_t_s:
                if map_t_s[chr_t]!=chr_s:
                    return False
            else:
                map_t_s[chr_t]=chr_s 

        return True