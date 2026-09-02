# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(node):
            nonlocal s
            
            if not node:
                return (float('inf'), float("-inf"), 0)

            leftMin, leftMax, leftSize = dfs(node.left)
            rightMin, rightMax, rightSize = dfs(node.right)

            if leftMax < node.val < rightMin:
                s = max(s, leftSize + rightSize + 1)
                return (min(leftMin, node.val), max(rightMax, node.val), leftSize + rightSize + 1)
            
            return (float('-inf'), float("inf"), 0)
            
        dfs(root)
        return s