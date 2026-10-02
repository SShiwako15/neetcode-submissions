# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        output = 0

        def dfs(temp):
            nonlocal output
            if temp == None:
                return 0
            left = dfs(temp.left)
            right = dfs(temp.right)
            diam = left + right
            output = max(output, diam)
            return 1 + max(right,left)

        dfs(root)
        return output