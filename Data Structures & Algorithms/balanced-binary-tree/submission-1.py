# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root):
            if root == None:
                return 0
            return 1 + max(getHeight(root.right),getHeight(root.left))
        
        if root == None:
            return True
        if abs(getHeight(root.right) - getHeight(root.left)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)
        