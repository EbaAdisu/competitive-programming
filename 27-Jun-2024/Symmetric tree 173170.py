# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(node1,node2):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                left = sym(node1.left,node2.right)
                right = sym(node1.right,node2.left)
                return left and right
            return not node1 and not node2
            
        return sym(root,root)