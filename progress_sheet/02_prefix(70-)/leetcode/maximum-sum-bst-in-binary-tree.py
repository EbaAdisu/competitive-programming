# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def valid(node):
            nonlocal ans
            if node:
                leftmax = valid(node.left)
                rightmin = valid(node.right)
                if leftmax[0] < node.val < rightmin[1]:
                    if leftmax[2] and rightmin[2]:
                        # print(leftmax,rightmin)
                        ans = max(ans,node.val+leftmax[3]+rightmin[3])
                    return max(leftmax[0],rightmin[0],node.val), min(rightmin[1],leftmax[1],node.val), leftmax[2] and rightmin[2],node.val+leftmax[3]+rightmin[3]
                return max(leftmax[0],rightmin[0],node.val), min(rightmin[1],leftmax[1],node.val), False,node.val+leftmax[3]+rightmin[3]
            return float('-inf'),float('inf'),True,0
        valid(root)
        return ans
