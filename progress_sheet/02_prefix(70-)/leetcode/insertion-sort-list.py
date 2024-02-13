# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        bu = True
        while bu:
            bu = False
            node = head
            pre = None
            while node and node.next:
                if node.val > node.next.val:
                    bu = True
                    if pre:
                        next = node.next
                        pre.next = node.next
                        node.next = next.next
                        next.next = node
                        pre = pre.next
                        node = pre.next
                    else:
                        next = node.next
                        node.next = next.next
                        next.next = node
                        head = next
                        pre = next
                        node = pre.next
                else:
                    pre = node
                    node = node.next

        return head