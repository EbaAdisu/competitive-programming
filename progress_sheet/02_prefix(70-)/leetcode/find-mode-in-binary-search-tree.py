# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = defaultdict(int)
        def trav(root):
            if root:
                modes[root.val]+=1
                trav(root.left)
                trav(root.right)
        trav(root)
        maxi = max(modes.values())
        ans = []
        for key in modes:
            if modes[key] == maxi:
                ans += [key]
        return ans
        