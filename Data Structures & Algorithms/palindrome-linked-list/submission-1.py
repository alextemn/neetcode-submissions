# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        fast, slow = head, head
        masterPrev = None
        while fast and fast.next:
            masterPrev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        masterPrev.next = prev

        fast, slow, cur = head, head, head
        while fast and fast.next:
            slow, cur = slow.next, cur.next
            fast = fast.next.next
        
        start = head

        while start != cur and slow:
            if start.val != slow.val:
                return False
            start = start.next
            slow = slow.next
        
        return True