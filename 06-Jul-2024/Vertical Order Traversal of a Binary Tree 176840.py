# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        verticals = defaultdict(list)
        def dfs(node,r,c):
            if node:
                verticals[c].append((r,node.val))
                dfs(node.left,r + 1, c - 1)
                dfs(node.right,r + 1, c + 1)
        dfs(root,0,0)
        ans = []
        for key in sorted(verticals):
            ans.append([e[1] for e in sorted(verticals[key])])
        return ans