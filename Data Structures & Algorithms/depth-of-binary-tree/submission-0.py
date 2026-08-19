# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = self.dfs(root)
        return count

    def dfs(self, root):
        if not root:
            return 0
        if root.left and root.right:
            return 1 + max(self.dfs(root.left), self.dfs(root.right))
        elif root.left:
            return 1 + self.dfs(root.left)
        elif root.right:
            return 1 + self.dfs(root.right)
        else:
            return 1
    