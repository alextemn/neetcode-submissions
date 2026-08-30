# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(n, val):
            nonlocal total
            val += str(n.val)
            
            if not n.left and not n.right:
                total += int(val)

            if n.left:
                dfs(n.left, val)
            if n.right:
                dfs(n.right, val)
        
        dfs(root, "")
        return total