# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def trav(node,k,count):
            if node:
                count = trav(node.left,k,count)
                try:
                    if count[1]: return count
                except:
                    count += 1
                if count == k:
                    # print(count,k)
                    return True,node.val
                count = trav(node.right,k,count)
                return count
            return count
        return trav(root,k,0)[1]
        