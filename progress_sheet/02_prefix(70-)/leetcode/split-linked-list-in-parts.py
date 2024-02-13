# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        p = n // k
        rem = n % k
        print(p,rem)
        ans = []
        dummy = head
        for i in range(k):
            temp = dummy
            t = 1 if rem else 0
            for i in range(p-1 + t):
                if not dummy:
                    break
                dummy = dummy.next

            if dummy:
                tempNode = dummy.next
                dummy.next = None
                dummy = tempNode
            else:
                dummy = None 
            rem = max(rem-1,0)
            ans.append(temp)
        return ans

            


        
        