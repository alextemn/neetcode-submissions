# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_di = 0
        queue = []
        queue.append(root)
        current = root
        while current:
            new_di = self.dfs(current.left) + self.dfs(current.right)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            if new_di > max_di:
                max_di = new_di
            if queue:
                queue.pop(0)
            if queue:
                current = queue[0]
            else:
                current = None
        return max_di

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