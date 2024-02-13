# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def rev (node):
            pre = None
            while node:
                temp = node.next
                node.next = pre
                pre = node
                node = temp
            return pre
        node = head
        for i in range(left-2):
            node = node.next
        if left == 1:
            reverse = node
        else:
            reverse = node.next 
        till = reverse
        for i in range(right-left):
            till = till.next
        
        if till:
            end = till.next 
            till.next = None
        else:
            end = None
        reverse = rev(reverse)
        if not reverse:
            return head 
        if left == 1:
            node = reverse
            head = node
        else:
            node.next = reverse
        while reverse.next:
            print(reverse,end)
            reverse = reverse.next
        reverse.next = end
        return head



        