# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        large = max(q.val,p.val)
        small = min(q.val,p.val)
        if root: 
            if small <= root.val <= large:
                return root
            if root.val > large:
                return self.lowestCommonAncestor(root.left, p, q)
            return self.lowestCommonAncestor(root.right, p, q)
        return None
                 
        