# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        canDo = False
        def sums(root11, root22):
            nonlocal canDo
            if not root11 or not root22:
                return
            if root11.val + root22.val > target:
                sums(root11.left, root22)
                sums(root11, root22.left)
            elif root11.val + root22.val < target:
                sums(root11.right, root22)
                sums(root11, root22.right)
            else:
                canDo = True
                return True
        sums(root1,root2)
        return canDo