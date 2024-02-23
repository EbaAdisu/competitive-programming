# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node):
            if node:
                if not node.right and not node.left:
                    return (node.val,node.val)
                left = float('-inf'),float('inf')
                right = float('-inf'),float('inf')
                if node.left:
                    left = isValid(node.left)
                    if left == False: return False
                if node.right:
                    right = isValid(node.right)
                    if right == False: return False
                if left[0]>= node.val  or node.val >= right[1]:
                    return False
                return max(left[0],right[0],node.val), min(left[1],right[1],node.val)
        return False if isValid(root) == False else True

    