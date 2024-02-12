# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        high = ListNode()
        part1 = less
        part2 = high
        node = head

        while node:
            if node.val < x:
                less.next = ListNode(node.val)
                less = less.next
            else:
                high.next = ListNode(node.val)
                high = high.next
            node = node.next
        less.next = part2.next
        # print(high,less,part2)
        return part1.next
        