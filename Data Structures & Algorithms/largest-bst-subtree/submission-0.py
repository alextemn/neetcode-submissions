# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(n):
            if not n:
                return (float('inf'), float('-inf'), 0)

            left = dfs(n.left)
            right = dfs(n.right)

            if left[1] < n.val < right[0]:
                min_val = min(n.val, left[0])
                max_val = max(n.val, right[1])
                size = left[2] + right[2] + 1

                return (min_val, max_val, size)

            return (float('-inf'), float('inf'), max(left[2], right[2]))

        return dfs(root)[2]