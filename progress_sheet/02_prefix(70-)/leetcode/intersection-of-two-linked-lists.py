# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(head):

            n = 0
            node = head
            while node:
                n += 1
                node = node.next
            return n
        length = length(headA) - length(headB)
        if length >= 0:
            longNode, shortNode = headA, headB
        else:
            longNode, shortNode = headB, headA
            length = -length
        while length:
            longNode = longNode.next
            length -= 1
        while longNode and shortNode:
            if longNode == shortNode:
                return longNode
            longNode = longNode.next
            shortNode = shortNode.next
        return None
        
