# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        if not root:
            return TreeNode(val)

        while cur:
            if not cur.left and cur.val > val:
                cur.left = TreeNode(val)
                break
            if not cur.right and cur.val < val:
                cur.right = TreeNode(val)
                break
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        
        return root