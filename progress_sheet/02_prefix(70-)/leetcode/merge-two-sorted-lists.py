# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        def recur(node1,node2,ans):
            if not node1:
                ans.next = node2
                return
            if not node2:
                ans.next = node1
                return
                
            if node1.val >= node2.val:
                small, large = node2, node1
            else:
                small, large = node1, node2
            next = small.next
            small.next, ans.next, node1, node2 = False, small, next, large
            ans = ans.next
            recur(node1,node2,ans)
        recur(list1,list2,ans)
        return head.next