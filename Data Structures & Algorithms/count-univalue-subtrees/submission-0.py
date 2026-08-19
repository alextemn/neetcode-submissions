# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        counts = 0

        def dfs(n):
            nonlocal counts
            if not n:
                return True
             
            l, r = dfs(n.left), dfs(n.right)

            if l and r:
                if n.left and n.val != n.left.val:
                    return False
                if n.right and n.val != n.right.val:
                    return False
                counts += 1
                return True
        dfs(root)
        return counts