# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        node = head
        n = length - n
        if n == 0:
            return head.next
        while node:
            if n == 0:
                prev.next = node.next
            prev = node    
            node = node.next
            n -= 1
        return head
            