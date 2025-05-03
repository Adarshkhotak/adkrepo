
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    maxi = float("-inf")

    def findMaxPathSum(self, root):
        if not root:
            return 0
        leftPathSum = max(0, self.findMaxPathSum(root.left))
        rightPathSum = max(0, self.findMaxPathSum(root.right))

        self.maxi = max(self.maxi, leftPathSum + root.val + rightPathSum)
        return max(leftPathSum, rightPathSum) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMaxPathSum(root)
        return self.maxi
    
#Coding NInja
# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
from math import *

maxi=float(-inf)
def findpathsum(root):
    
    if not root:
        return 0
    ls= max(0, findpathsum(root.left))
    rs= max(0, findpathsum(root.right))
    global maxi
    maxi = max(maxi , rs+ls+root.data)
    return max(ls,rs)+root.data

def maxPathSum(root: BinaryTreeNode) -> int:
    findpathsum(root)
    return maxi
    
