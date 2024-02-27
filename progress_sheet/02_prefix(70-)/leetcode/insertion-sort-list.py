# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        curr = head
        t = 0
        while curr:
            first = head
            for i in range(t):
                if first.val > curr.val:
                    first.val, curr.val = curr.val, first.val
                first = first.next
            curr = curr.next
            t += 1
        return head