# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq = {}
        cur = head
        dels = head
        prev = None

        while cur:
            freq[cur.val] = freq.get(cur.val, 0) + 1
            cur = cur.next

        while dels:
            if freq[dels.val] > 1:
                temp = dels.next
                
                if prev:
                    prev.next = temp
                else:
                    head = temp
            else:
                prev = dels
            
            dels = dels.next
        
        return head