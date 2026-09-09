# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        def recurse(node):
            nonlocal cur
            if not node:
                return True
            
            n = recurse(node.next)

            if node.val != cur.val:
                return False
            
            cur = cur.next
            return n
        
        return recurse(head)