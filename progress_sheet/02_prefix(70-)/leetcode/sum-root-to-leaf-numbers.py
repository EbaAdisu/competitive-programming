# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNum(root,ans):
            if not root.left and not root.right:
                return ans + root.val
            left = right = 0
            if root.left:
                left = sumNum(root.left,(ans+root.val)*10)
            if root.right:
                right = sumNum(root.right,(ans+root.val)*10)
            return left + right
        return sumNum(root,0)
