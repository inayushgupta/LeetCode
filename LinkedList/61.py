# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        l = 1
        curr = head
        while curr.next:
            curr = curr.next
            l += 1
        
        k = k%l
        if k == 0:
            return head
        
        # now the list is cyclic
        curr.next = head

        # now we move l-k steps and split the list
        prev, newhead = None, head
        for _ in range(l-k):
            prev = newhead
            newhead = newhead.next
        
        prev.next = None
        return newhead
        

