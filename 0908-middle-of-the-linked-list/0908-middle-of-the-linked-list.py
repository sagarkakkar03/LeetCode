# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next 
        target = length//2+1
        ans = None
        node = head
        while target:
            ans = node
            target -= 1
            node = node.next
        return ans