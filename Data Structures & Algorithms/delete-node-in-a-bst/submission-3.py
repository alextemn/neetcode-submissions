# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(n, parent):
            if not n:
                return (None, None)
            if n.val == key:
                return (n, parent)
            
            left = dfs(n.left, n)
            right = dfs(n.right, n)

            if n.val > key:
                return left
            
            return right

        cur, parent = dfs(root, None)
        if not cur:
            return root
        
        if not cur.left or not cur.right:
            if not cur.left:
                replace = cur.right
            elif not cur.right:
                replace = cur.left
            
            if not parent:
                return replace
            if parent.left == cur:
                parent.left = replace
            else:
                parent.right = replace
            
            return root

        sParent = cur
        s = cur.right

        while s.left:
            sParent = s
            s = s.left
        cur.val = s.val
        
        if sParent.left == s:
            sParent.left = s.right
        else:
            sParent.right = s.right

        return root