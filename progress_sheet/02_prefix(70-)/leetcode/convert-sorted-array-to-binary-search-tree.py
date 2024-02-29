# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.binary(0,len(nums)-1,nums)
    def binary(self,l,r,nums):
        if l > r:
            return None
        if l == r:
            return TreeNode(nums[l])
        mid = (l+r)//2
        ans = TreeNode(nums[mid])
        ans.left = self.binary(l,mid-1,nums)
        ans.right = self.binary(mid+1,r,nums)
        return ans
