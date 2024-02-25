# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def trav(node,large, small,ans):
            if node:
                left = trav(node.left,large,small,ans)
                llarge,lsmall,lans = left
                llarge = max(node.val,llarge)
                lsmall = min(node.val,lsmall)
                lans = max(lans,abs(node.val - lsmall),abs(node.val - llarge))

                right = trav(node.right,large,small,ans)
                rlarge,rsmall,rans = right
                rlarge = max(node.val,rlarge)
                rsmall = min(node.val,rsmall)
                rans = max(rans,abs(node.val - rsmall),abs(node.val - rlarge))
                large,small,ans = max(llarge,rlarge),min(lsmall,rsmall),max(lans,rans)
            return large,small,ans
        print(trav(root,0,float('inf'),0))
        return trav(root,0,float('inf'),0)[2]

        