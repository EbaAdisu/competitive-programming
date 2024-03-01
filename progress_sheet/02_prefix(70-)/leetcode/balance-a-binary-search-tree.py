# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        li = []
        def preList(root,li):
            if root:
                preList(root.left,li) 
                li.append(root.val)
                preList(root.right,li)
            return li
        def binary(l,r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            mid = (l+r)//2
            ans = TreeNode(nums[mid])
            ans.left = binary(l,mid-1)
            ans.right = binary(mid+1,r)
            return ans
        nums = preList(root,[])
        print(nums)
        return binary(0,len(nums)-1)