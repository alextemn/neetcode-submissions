"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        newRoot = Node(root.val)
        queue = collections.deque()
        queue.append((root, newRoot))

        while queue:
            qLen = len(queue)

            for i in range(qLen):
                old, new = queue.popleft()
                for j in range(len(old.children)):
                    new.children.append(Node(old.children[j].val))
                    queue.append((old.children[j], new.children[j]))
        
        return newRoot
