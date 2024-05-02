# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        count = 0
        node1 = head1
        node2 =  head2
        while node1 != node2:
            if count == 2:
                return None
            node1 = node1.next
            node2 = node2.next
            if node1 == None:
                node1 = head2
                count += 1
            if node2 == None:
                node2 = head1
        return node1