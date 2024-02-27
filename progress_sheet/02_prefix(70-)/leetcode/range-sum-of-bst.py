# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangeSum(root,ans):
            if root:
                if low <= root.val <= high:
                    ans += root.val
                ans = rangeSum(root.left,ans)
                ans = rangeSum(root.right,ans)
            return ans
        return rangeSum(root,0)
    