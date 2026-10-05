# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        
        while q:
            lenq = len(q)
            rightmost = None

            for _ in range(lenq):
                curr = q.popleft()
                if curr:
                    rightmost = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if rightmost:
                res.append(rightmost.val)
        return res