# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        pre = None
        while node:
            if pre and node.val == pre.val:
                pre.next = node.next
                node = node.next
            else:
                pre = node
                node = node.next

        return head
