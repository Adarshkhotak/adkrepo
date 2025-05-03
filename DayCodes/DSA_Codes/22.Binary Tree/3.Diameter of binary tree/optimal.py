
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Time Complexity: O(N)
Space Complexity : O(1) as no additional data structures or 
memory is allocated.O(H)
"""
from typing import Optional
class Solution:
    diameter = 0

    def calculateHeight(self, root):
        if not root:
            return 0
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateHeight(root)
        return self.diameter


#FOR Coding ninja
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
daimeter=0
def calheight(root):
    if not root:
        return 0
    lh= calheight(root.left)
    rh = calheight(root.right)
    global daimeter
    daimeter = max( daimeter , lh+rh)
    return 1 + max(lh,rh)

def diameterOfBinaryTree(root: TreeNode) -> int:
    calheight(root)
    return daimeter