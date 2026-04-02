"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        if not head:
            return None

        old_to_new = {None: None}

        curr = head
        dummy = tail = Node(0, None, None)

        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            tail.next = new_node
            tail = tail.next
            curr = curr.next

        curr = head
        tail = dummy.next

        while curr:
            tail.random = old_to_new[curr.random]
            tail = tail.next
            curr = curr.next

        return dummy.next

