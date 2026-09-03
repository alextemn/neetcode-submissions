# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append((root, 0))
        res = {}
        MIN, MAX = float('inf'), float('-inf')

        while queue:
            q_len = len(queue)
            for i in range(q_len):
                n = queue.popleft()
                col = n[1]

                MIN, MAX = min(MIN, col), max(MAX, col)
                if col in res:
                    res[col].append(n[0].val)
                else:
                    res[col] = [n[0].val]

                if n[0].left:
                    queue.append((n[0].left, col - 1))
                if n[0].right:
                    queue.append((n[0].right, col + 1))
        output = []
        for i in range(MIN, MAX + 1):
            if i in res:
                output.append(res[i])
        
        return output