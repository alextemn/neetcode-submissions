# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = list1
        if not list1:
            start = list2
        elif not list2:
            start = list1
        elif list1.val > list2.val:
            start = list2
        prev = None
        cur = list1
        comp = list2
        while cur and comp:
            if cur.val > comp.val:
                if prev:
                    prev.next = comp
                temp = cur
                cur = comp
                comp = temp
            if cur.next is None:
                cur.next = comp
                break
            if cur.val <= comp.val:
                prev = cur
                cur = cur.next
        return start