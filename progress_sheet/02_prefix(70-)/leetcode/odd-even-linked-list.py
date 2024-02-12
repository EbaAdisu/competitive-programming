# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head.next
        node = head
        part = node
        t = 0
        while node.next:
            temp = node.next
            node.next = temp.next
            node = temp
            t += 1
            if not t%2:
                part = node
        part.next = odd
        return head
