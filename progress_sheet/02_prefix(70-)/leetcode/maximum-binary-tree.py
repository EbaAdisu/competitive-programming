# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def binary(num):
            if not num:
                return None
            maxi = max(num)
            ind = num.index(maxi)
            ans = TreeNode(maxi)
            ans.left = binary(num[:ind])
            ans.right = binary(num[ind+1:])
            return ans
        return binary(nums)