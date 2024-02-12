# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
            dummy = dummy.next
        while list1:
            dummy.next = ListNode(list1.val)
            list1 = list1.next
            dummy = dummy.next
        while list2:
            dummy.next = ListNode(list2.val)
            list2 = list2.next
            dummy = dummy.next
        return ans.next