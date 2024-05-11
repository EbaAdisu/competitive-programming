# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def trav(root):
            if root:
                left = trav(root.left)
                right = trav(root.right)
                child = left[1] + right[1] + root.val
                grandchild = left[0] + right[0]
                return max(child, grandchild), (grandchild)
            return 0,0
        return trav(root)[0]
        