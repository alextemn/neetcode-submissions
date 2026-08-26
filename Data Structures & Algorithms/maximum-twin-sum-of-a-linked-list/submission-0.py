# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        f, s = head, head
        stack = []
        res = 0

        while f:
            stack.append(s)

            s = s.next
            f = f.next.next
        
        while s:
            res = max(res, s.val + (stack.pop()).val)
            s = s.next
        
        return res