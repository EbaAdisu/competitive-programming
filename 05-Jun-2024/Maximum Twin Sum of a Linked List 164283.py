# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast, pre = head, head, None

        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        ans = 0
        while pre:
            ans = max(ans, pre.val+ slow.val)
            pre, slow = pre.next, slow.next
        return ans
