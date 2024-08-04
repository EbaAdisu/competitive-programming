# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        N = 0
        left = head
        right = head
        vals = []
        while right:
            vals.append(right.val)
            right = right.next
            N += 1
            if N == k:
                while vals:
                    left.val = vals.pop()
                    left = left.next
                N = 0
        return head
            



        