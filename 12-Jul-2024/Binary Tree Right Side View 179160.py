# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        col = defaultdict(int)
        depth = 0

        def trav(root,d):
            nonlocal depth
            if root:
                depth = max(depth,d)
                if d not in col:
                    col[d] = root.val
                trav(root.right,d + 1)
                trav(root.left,d + 1,)
            return
        trav(root,0)
        ans = [0] * (depth + 1) 
        for key in col:
            ans[key] = col[key]
        # print(col,depth)
        return ans
