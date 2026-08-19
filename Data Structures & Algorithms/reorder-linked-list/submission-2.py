# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur, second = head, head
        
        while cur and cur.next:
            cur = cur.next.next
            second = second.next
        
        nxt = None
        start = second
        while start:
            temp = start.next
            start.next = nxt
            nxt = start
            start = temp
        new = head
        second = nxt
        while new.next and second.next:
            temp = new.next
            temp2 = second.next
            
            new.next = second
            second.next = temp

            new = temp
            second = temp2