# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        f, s = head, head
        first = head
        res = 0
        prev = None
        while f and f.next:
            f = f.next.next
            temp = s.next
            s.next = prev
            prev = s
            s = temp
        first.next = s
        
        start = prev

        while s:
            res = max(res, s.val + start.val)
            s = s.next
            start = start.next
        return res