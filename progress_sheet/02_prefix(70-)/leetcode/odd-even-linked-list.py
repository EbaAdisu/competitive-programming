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
        while node.next:
            temp = node.next
            node.next = temp.next
            node = temp
        node = head
        while node.next:
            node = node.next
        node.next = odd
        return head
