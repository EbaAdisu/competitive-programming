# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def dup(head):
            node = ListNode()
            ans = node
            dummy = head
            while dummy:
                node.next = ListNode(dummy.val)
                node = node.next
                dummy = dummy.next
            return ans.next
        node = dup(head)
        pre = None
        while node:
            temp = node
            node = node.next
            temp.next = pre
            pre = temp
        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True