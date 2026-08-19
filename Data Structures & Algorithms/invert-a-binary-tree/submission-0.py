# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []
        queue.append(root)
        if not root:
            return root

        while queue:
            node = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp
            
            queue.pop(0)
        return root