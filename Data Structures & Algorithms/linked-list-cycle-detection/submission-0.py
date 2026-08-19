# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        el_count = {}
        while head:
            #print(el_count[head])
            el_count[head] = 1 + el_count.get(head, 0)
            if el_count[head] > 1:
                print(el_count[head])
                return True
            head = head.next
        return False
            