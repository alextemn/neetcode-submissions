# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nNode, end = head, head
        prev = None
        for i in range(n):
            end = end.next
        
        while end:
            prev = nNode
            nNode = nNode.next
            end = end.next
        
        if prev:
            prev.next = nNode.next
            nNode.next = None
        elif not prev and nNode.next:
            head = head.next
        else:
            return None
        return head