class Solution(object):
    def maxDepth(self, s):
        curr_depth=0
        max_depth=0
        for brac in s :
            if brac=="(":
                curr_depth+=1
                max_depth=max(curr_depth,max_depth)
            elif brac==")":
                curr_depth-=1
        return max_depth