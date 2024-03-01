# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def trav(node,count):
            if node:
                left_count = trav(node.left,count)
                if left_count[0]:
                    return left_count
                if left_count[1] + 1 == k:
                    return True,node.val
                return trav(node.right,left_count[1]+1)
            return False, count
        return trav(root,0)[1]
            