# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        node = head
        curr = ans
        node = node.next
        while node:
            num = 0
            while node.val != 0:
                num += node.val
                node = node.next
            node = node.next
            curr.val = num
            if node:
                curr.next = ListNode()
                curr = curr.next
        return ans
        