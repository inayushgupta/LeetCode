# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        dummy = tail = ListNode(float('-inf'), head)
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                dup = curr.val
                while curr and curr.val == dup:
                    curr = curr.next
                tail.next = curr
            else:
                tail = curr
                curr = curr.next

        return dummy.next
        
